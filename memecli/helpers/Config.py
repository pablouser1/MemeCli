import json
from os.path import isdir

def getConfig(path: str)-> dict:
    if isdir(path):
        # Import JSON config
        f = open(path + "/config.json")
        config_string = f.read()
        config = json.loads(config_string)
        f.close()
        return config
    else:
        raise Exception('Template not found')
