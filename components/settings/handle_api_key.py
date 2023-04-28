import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from dotenv import find_dotenv, load_dotenv
from components.settings.restart_popup import show_restart_popup, restart_app

load_dotenv()

class HandleAPIKey:
    def __init__(self, master):
        api_key = os.getenv('OPENAI_API_KEY')

        style = ttk.Style()
        style.configure('TLabel', background='#2c2f33', foreground='#ffffff')
        style.configure('TEntry', background='#2c2f33', foreground='#ffffff', fieldbackground='#2c2f33', insertcolor='#ffffff')
        style.configure('TButton', background='#43b581', foreground='#ffffff', bordercolor='#43b581')
        style.map('TButton', background=[('active', '#3aa76d'), ('pressed', '#3aa76d')])

        self.master = master

        masked_api_key = self.mask_api_key(api_key)
        self.api_key_label = ttk.Label(master, text=f"OPENAI API KEY: {masked_api_key}", style='TLabel')
        self.api_key_label.pack(pady=10)

        self.api_key_entry = ttk.Entry(master, style='TEntry', font=('TkDefaultFont', 15))
        self.api_key_entry.insert(0, "Update API Key")
        self.api_key_entry.pack(pady=10)

        self.save_button = ttk.Button(master, text="Save API Key", command=self.save_api_key, style='TButton')
        self.save_button.pack(pady=10)

    def save_api_key(self):
        new_api_key = self.api_key_entry.get()
        dotenv_path = find_dotenv() or ".env"
        with open(dotenv_path, "w") as env_file:
            env_file.write(f"OPENAI_API_KEY={new_api_key}")
        self.api_key_entry.delete(0, 'end')
        masked_api_key = self.mask_api_key(new_api_key)
        self.api_key_label.config(text=f"OPENAI_API_KEY: {masked_api_key}")

        # Show a popup window with a restart message and a "RESTART" button
        show_restart_popup(self.master, restart_app)

    def mask_api_key(self, api_key):
        if api_key:
            half_length = len(api_key) // 2
            return api_key[:half_length] + '*' * (len(api_key) - half_length)
        return None

    def show_restart_popup(self):
        restart_popup = tk.Toplevel(self.master)
        restart_popup.title("Restart Required")
        restart_popup.geometry("300x100")

        restart_message = ttk.Label(restart_popup, text="You must restart the program for changes to take effect.")
        restart_message.pack(pady=10)

        restart_button = ttk.Button(restart_popup, text="RESTART", command=self.restart_app)
        restart_button.pack(pady=5)

    def restart_app(self):
        os.execv(sys.executable, ['python'] + sys.argv)
