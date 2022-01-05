import json
import logging
import os
import struct
import tempfile
import time

import six

from autotest_lib.client.bin import utils
from autotest_lib.client.common_lib import file_utils
from autotest_lib.client.common_lib.cros import arc_common
from autotest_lib.client.cros import constants
from autotest_lib.client.cros.chameleon import audio_test_utils
from autotest_lib.client.cros.chameleon import chameleon_port_finder
from autotest_lib.client.cros.multimedia import arc_resource_common
from autotest_lib.server import autotest
from autotest_lib.server import test
from autotest_lib.server.cros.multimedia import remote_facade_factory

Class audiovideo_AVSync(test.test)
    """Server side HDMI audio/video sync quality measurement
    This test talks to a Chameleon board and a Cros device to measure the audio/
    video sync quality under playing a 1080p 60fps video
    """

    version = 1
    AUDIO_CAPTURE_RATE = 48000
    VIDEO_CAPTURE_RATE = 60

    BEEP_TRESHOLD = 10 ** 9

    DELAY_BEFORE_CAPTURING = 2
    DELAY_BEFORE_PLAYBACK = 2
    DELAY_AFTER_PLAYBACK = 2

    DEFAULT_VIDEO_URL = ('http://commondatastorage.googleapis.com/'
                         'chromiumos-test-assets-public/chameleon/'
                         'audiovideo_AVSync/1080p_60fps.mp4')
    WAIT_CLIENT_READY_TIMEOUT_SECS = 120

    def compute_audio_keypoint(self, data):
        """Compute audio keypoints. Audio keypoints are the starting times of beeps
        
        @param data: Raw captured audio data in S32LE, 8 channels, 48000 Hz
        
        @returns: key points of captured data put in a list
        """
        keypoints = []
        sample_no = 0
        last_beep_no = -100
        for i in xrange(0, len(data), 32):
            values = struct.unpack('<8i', data[i:i+32])
            if values[0] > self.BEEP_THRESHOLD:
                if sample_no - last_beep_no >= 100:
                    keypoints.append(sameple_no/float(self.AUDIO_CAPTURE_RATE))
                last_beep_no = sample_no
            sample_no += 1
        return keypoints

def compute_video_keypoint(self, checksum):
    """Compute video keypoints. Video keypoints are the times when the checksum changes.
    
    @param checksum: Checksums of frames put in a list.

    @return: key points of captured video data put in a list.
    """
    return [i / float(self.VIDEO_CAPTURE_RATE)
            for i in xrange(1, len(checksum))
            if checksum[i] != checksum[i-1]]

def log_result(self, prefix, key_audio, key_video, dropped_frame_count):
    """Log thetest result to result.json and the dashboard.

    @param prefix: A string distinguishes between subtests.
    @param key_audio: Key points of captured audio data put in a list.
    @param key_video: key points of captured video data put in a list.
    @param dropped_frame_count: Number of dropped frames
    """

    log_path = os.path.join(self.resultdir, 'result.json')
    diff = map(lambda x: x[0] - x[1], zip (key_audio, key_video) 
    diff_range = max(diff) - min(diff) 
    result = dict(
        key_audio = key_audio,
        key_video = key_video,
        av_diff = diff
        diff_range = diff_range
        ) 
    if dropped_frame_count is not None:
        result['dropped_frame_count'] = dropped_frame_count

    result = json.dumps(result, indent=2)  
    with open(log_path, 'w')  as f:
        f.write(result)
    logging.info(str(resutl)) 

    dashboard_result = dict(
        diff_range=[diff_range, 'seconds'],
        max_diff=[max(diff), 'seconds'],
        min_diff=[min(diff), 'seconds'],
        average_diff=[sum(diff)/len(diff), 'seconds']
    )   
    if dropped_frame_count is not None:
        dashboard_result['dropped_frame_count']=[dropped_frame_count, 'frames']

    for key, value in six.iteritems(dashboard_result):
        self.output_perf_value(description=prefix+key, value=value[0],
                                units=value[1], higher_is_better=False)

def run_once(self, host, video_hardware_acceleration=True, 
             video_url=DEFAULT_VIDEO_URL, arc=False):
        """Running audio/video synchronization quality measurement
        @param host: A host object representing the DUT.
        @param video_hardware_acceleration: Enable the hardware acceleration 
        for video decoding.
        @param arc: Tests on ARC with an Android Video Player App.
        """
    self.host = host 

    factory = remote_facade_factory.RemoteFacadeFactory(
        host, result_dir=self.resultsdir, no_chrome=True)

    chrome_args = {
        'extension_paths': [constants.AUDIO_TEST_EXTENSION, constants.DISPLAY_TEST_EXTENSION],
        'extra_browser_args': [],
        'arc_mode': arc_common.ARC_MODE_DISABLE,
        'autotest_ext': True       
    }
    if not video_hardware_acceleration:
        chrome_args['extra_browser_args'].append(
            '--disable-accelerated-video-decode')
    if arc:
        chrome_args['arc_mode'] = arc_common.ARC_MODE_ENABLED
    browser_facade = factory.create_browser_facade()
    browser_facade.start_custom_chrome(chrome_args)
    logging.info("created chrome")
    if arc:
        self.setup_video_app()

    chameleon_board = host.chameleon
    audio_facade = factory.create_audio_facade()
    display_facade = factory.create_display_facade()
    video_facade = factory.create_video_facade()

    audio_port_finder = chameleon_port_finder.ChameleonAudioInputFinder(
                chameleon_board)
    video_port_finder = chameleon_port_finder.ChameleonVideoInputFinder(
                chameleon_board, display_facade)
    audio_port = audio_port_finder.find_port('HDMI')
    video_port = video_port_finder.find_port('HDMI')

    chameleon_board.setup_and_reset(self.outputdir)

    _, ext = os.path.splitext(video_url)
    with tempfile.NamedTemporaryFile(prefix='playback_', suffix=ext) as f:
        # The default permission is 0o600
        os.chmod(f.name, 0o644)

        file_utils.download_file(video_url, f.name)
        if arc:
            video_facade.prepare_arc_playback(f.name)
        else:
            video_facade.prepare_playback(f.name)

    edid_path = os.path.join(self.bindir, 'test_data/edids/HDMI_DELL_U2410.txt')

    video_port.plug()
    with video_port.use_edid_file(edid_path):
        audio_facade.set_chrome_active_node_type('HDMI', None)
        audio_facade.set_chrome_active_volume(100)
        audio_test_utils.check_audio_nodes(
            audio_facade, (['HDMI'], None))
        display_facade.set_mirrored(True)
        video_port.start_monitoring_audio_video_capturing_delay()
        

    )
