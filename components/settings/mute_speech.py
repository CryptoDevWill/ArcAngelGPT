import tkinter.ttk as ttk

class MuteSpeech:
    def __init__(self, master):
        self.mute_button = ttk.Button(master, text="Mute Speech", command=self.toggle_mute)
        self.mute_button.pack(padx=10, pady=10, anchor='n')

        self.mute_speech = False

    def toggle_mute(self):
        self.mute_speech = not self.mute_speech
        if self.mute_speech:
            self.mute_button.config(text="Unmute Speech")
        else:
            self.mute_button.config(text="Mute Speech")
