import json

class Settings:
    font = ''

    def __init__(self):
        f = open('settings.json')
        settings_string = f.read()
        final = json.loads(settings_string)
        self.font = final["font"]
