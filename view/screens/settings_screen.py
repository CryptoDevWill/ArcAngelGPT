import tkinter as tk
import tkinter.ttk as ttk
from view.gui.settings_window.mute_speech import MuteSpeech
from view.gui.handle_api_key import HandleAPIKey
from controller.utils.load_settings import load_settings


class SettingsScreen:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        self.handle_api_key = HandleAPIKey(self.frame)
        self.settings = load_settings()

        self.mute_speech = MuteSpeech(self.frame, self.settings)
        self.mute_speech.pack()

    def show(self):
        self.frame.lift()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.title('Settings')
    settings_screen = SettingsScreen(root)
    settings_screen.show()
