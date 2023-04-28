import tkinter as tk
import tkinter.ttk as ttk
from components.settings.mute_speech import MuteSpeech
from components.settings.handle_api_key import HandleAPIKey


class SettingsScreen:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        self.handle_api_key = HandleAPIKey(self.frame)
        self.mute_speech = MuteSpeech(self.frame)

    def show(self):
        self.frame.lift()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.title('Settings')
    settings_screen = SettingsScreen(root)
    settings_screen.show()
