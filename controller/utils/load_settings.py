import os
import json

def load_settings():
    settings_file = 'settings.json'

    # Check if the settings file exists, and create it with default values if not
    if not os.path.isfile(settings_file):
        default_settings = {
            'api_key': '',
            'mute_speech': False,
            'default_voice': 'en-US',
            'output_voice_speed': 1.0,
            'working_directory': os.getcwd() + "/working_directory"
        }
        with open(settings_file, 'w') as f:
            json.dump(default_settings, f, indent=4)

    # Load the settings file and return the settings
    with open(settings_file) as f:
        settings = json.load(f)
    return settings
