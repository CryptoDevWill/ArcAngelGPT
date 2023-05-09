import json
import tkinter.ttk as ttk

class MuteSpeech:
    def __init__(self, master, settings):
        self.mute_button = ttk.Button(master, text="Mute Speech", command=self.toggle_mute)
        self.mute_button.pack(padx=10, pady=10, anchor='n')

        self.mute_speech = settings.get('mute_speech', False)

    def save_settings(self):
        settings = {'mute_speech': self.mute_speech}
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

    def pack(self, **kwargs):
        self.mute_button.pack(**kwargs)

    def toggle_mute(self):
        self.mute_speech = not self.mute_speech
        if self.mute_speech:
            self.mute_button.config(text="Unmute Speech")
        else:
            self.mute_button.config(text="Mute Speech")
        self.save_settings()