import logging
import os
import time

#try except for input an integer/number
def int_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError as e:
            print("Not a proper integer! Try it again")

# doesn't use f.open() and f.close()
with open("text.txt", "r") as fh:
    for line in fh:
        print(line.strip())

# if the file is small and we need to replace certain string, we don't need to read line by line
txt=open("text.txt","r")
text=txt.read
print(txt.read())
txt=txt.replace("put","puut")
#txt=txt.replace("puor","pur")
#with open("new_text.txt","w") as fh:
   # fh.write(txt)
   # print(new_text.txt)



