import os
import tkinter as tk
import tkinter.ttk as ttk
from dotenv import load_dotenv, set_key, find_dotenv
from functions.speak import mute_button

dotenv_path = find_dotenv()
if not dotenv_path:
    with open(".env", "w") as env_file:
        env_file.write("OPENAI_API_KEY=")

load_dotenv()

class SettingsScreen:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        style = ttk.Style()
        style.configure('TButton', background='#43b581', foreground='#ffffff', bordercolor='#43b581')
        style.map('TButton', background=[('active', '#3aa76d'), ('pressed', '#3aa76d')])
        style.configure('TEntry', background='#2c2f33', foreground='#ffffff', fieldbackground='#2c2f33', insertcolor='#ffffff')

        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            self.api_key_label = tk.Label(self.frame, text="Enter API key:", bg='#2c2f33', fg='#ffffff')
        else:
            masked_api_key = self.mask_api_key(self.api_key)
            self.api_key_label = tk.Label(self.frame, text=f"OPENAI_API_KEY: {masked_api_key}", bg='#2c2f33', fg='#ffffff')
        self.api_key_label.pack(pady=10)

        self.api_key_entry = ttk.Entry(self.frame, style='TEntry', font=('TkDefaultFont', 15))
        self.api_key_entry.insert(0, "Update API Key")
        self.api_key_entry.pack(pady=10)

        self.save_button = ttk.Button(self.frame, text="Save API Key", command=self.save_api_key, style='TButton')
        self.save_button.pack(pady=10)

        self.status_label = tk.Label(self.frame, text="", bg='#2c2f33', fg='#ffffff')
        self.status_label.pack(pady=10)

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

    def save_api_key(self):
        new_api_key = self.api_key_entry.get()
        if new_api_key != self.api_key:
            with open(dotenv_path or ".env", "w") as env_file:
                env_file.write(f"OPENAI_API_KEY={new_api_key}")
            self.api_key = new_api_key
            self.api_key_entry.delete(0, 'end')
            masked_api_key = self.mask_api_key(self.api_key)
            self.api_key_label.config(text=f"OPENAI_API_KEY: {masked_api_key}")
            self.status_label.config(text="API key updated")

    def mask_api_key(self, api_key):
        if api_key:
            half_length = len(api_key) // 2
            return api_key[:half_length] + '*' * (len(api_key) - half_length)
        return None

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.title('Settings')
    settings_screen = SettingsScreen(root)
    settings_screen.show()

