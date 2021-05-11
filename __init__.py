from mycroft import MycroftSkill, intent_file_handler


class EmploymentConditions(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('conditions.employment.intent')
    def handle_conditions_employment(self, message):
        self.speak_dialog('conditions.employment')


def create_skill():
    return EmploymentConditions()

