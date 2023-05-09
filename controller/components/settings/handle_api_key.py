import os
import tkinter as tk
import tkinter.ttk as ttk
from dotenv import find_dotenv
from controller.components.settings.restart_popup import show_restart_popup

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
        self.api_key_entry.pack(pady=10)

        self.enter_api_key_button = ttk.Button(master, text="Enter OpenAI API Key", command=self.initiate_agreement, style='TButton')
        self.enter_api_key_button.pack(pady=10)

    def initiate_agreement(self):
        new_api_key = self.api_key_entry.get()
        show_restart_popup(self.master, new_api_key)

    def mask_api_key(self, api_key):
        if api_key:
            half_length = len(api_key) // 2
            return api_key[:half_length] + '*' * (len(api_key) - half_length)
        return None