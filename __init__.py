from mycroft import MycroftSkill, intent_file_handler


class Blink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blink.intent')
    def handle_blink(self, message):
        self.speak_dialog('blink')


def create_skill():
    return Blink()

