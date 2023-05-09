import json

def load_settings():
    with open('data\settings.json') as f:
        settings = json.load(f)
    return settings