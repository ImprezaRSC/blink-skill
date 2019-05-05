from mycroft import MycroftSkill, intent_file_handler
import time
#import RPi.GPIO as GPIO
import subprocess as sub

class Blink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blink.intent')
    def handle_blink(self, message):
        self.speak_dialog('blink')

        #GPIO.setmode(GPIO.BOARD)
        #green=11
        #GPIO.setup(green,GPIO.OUT)
        #GPIO.output(green,True)
        #time.sleep(1)
        #GPIO.output(green,False)
        #time.sleep(1)
        #GPIO.output(green,True)
        #time.sleep(1)
        #GPIO.output(green,False)
        s = "./blink.c"
        subprocess.call([s],shell=True)
        time.sleep(5)
        #GPIO.cleanup()

def create_skill():
    return Blink()

