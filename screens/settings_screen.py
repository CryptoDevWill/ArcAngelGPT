import os
import tkinter as tk
from dotenv import load_dotenv
from functions.speak import mute_button

load_dotenv()

class SettingsScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        # Create a mute button
        self.api_key_label = tk.Label(self.frame, text="Speech Mode: ")
        self.api_key_label.pack(side=tk.LEFT, pady=10, anchor=tk.N)

        self.mute_button = tk.Button(self.frame, text="Mute Speech", command=self.toggle_mute)
        self.mute_button.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.N)
        # Set the initial mute state to False
        self.mute_speech = False


    def show(self):
        self.frame.lift()

    def toggle_mute(self):
        self.mute_speech = not self.mute_speech
        if self.mute_speech:
            mute_button(True)
            self.mute_button.config(text="Unmute Speech")
        else:
            mute_button(False)
            self.mute_button.config(text="Mute Speech")

# Create a Tkinter window and display the SettingScreen
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.title('Settings')
    settings_screen = SettingsScreen(root)
    settings_screen.show()
    root.mainloop()