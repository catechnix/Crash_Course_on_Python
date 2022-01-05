import logging
import os
import time

from autotest_lib.client.cros.audio import audio_test_data
from autotest_lib.client.cros.chameleon import audio_test_utils
from autotest_lib.client.cros.chameleon import chameleon_audio_ids
from autotest_lib.cllient.cros.audio import audio_test

class audio_AudioBasicInternalSpeaker(audio_test.AudioTest):
    '''Service site internal speaker audio test.
    This test talks to a Chameleon board and a Cros device to verify internal 
    speaker audio function of the Cros device
    '''
    version = 1
    DELAY_BEFORE_RECORD_SECONDS = 0.5
    RECORD_SECORDS = 8
    
    def run_once(self):
        """Runs basic audio speaker test."""
        if not audio_test_utils.has_internal_speaker(self.host):
            return
        
        golden_file = audio_test_data.GenerateAudioTestData(
            path=os.path.join(self.bindir, 'fix_440_16_0.5.raw'),
            duration_secs=10,
            frequencies=[440,440],
            volume_scale=0.5)

        source = self.widget_factory.create_widget(chameleon_audio_ids.CrosIds.SPEAKER)
    
        recorder = self.widget_factory.create_widget(chameleon_audio_ids.CrosIds.MIC)

        audio_test_utils.dump_cros_audio_logs(self.host, self.facade, self.resultdir, 'start')

        

        )
