from mycroft import MycroftSkill, intent_file_handler
import time
import subprocess

class Blink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blink.intent')
    def handle_blink(self, message):
        self.speak_dialog('blink')

        s = "/opt/mycroft/skills/blink-skill/blink"
        subprocess.run([s],shell=True)
        time.sleep(5)

def create_skill():
    return Blink()

