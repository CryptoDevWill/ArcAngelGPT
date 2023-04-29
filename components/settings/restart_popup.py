import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from dotenv import load_dotenv, find_dotenv
from functions.play_sound import play_sound
def show_restart_popup(master, new_api_key):
    play_sound("system")
    restart_popup = tk.Toplevel(master)
    restart_popup.title("Restart Required")
    restart_popup.geometry("400x150")
    restart_popup.configure(bg='#2c2f33')

    style = ttk.Style()
    style.configure('TLabel', background='#2c2f33', foreground='#ffffff')
    style.configure('TButton', background='#43b581', foreground='#ffffff', bordercolor='#43b581')
    style.map('TButton', background=[('active', '#3aa76d'), ('pressed', '#3aa76d')])

    terms_conditions = "By clicking 'Agree and Reset API Key', you agree that ArcAngelAI is an experimental program and should be used at your own risk. ArcAngelAI is not liable for any damages."
    terms_label = ttk.Label(restart_popup, text=terms_conditions, wraplength=350, style='TLabel')
    terms_label.pack(pady=10)

    agree_button = ttk.Button(restart_popup, text="Agree and Reset API Key", command=lambda: save_api_key_and_restart(new_api_key), style='TButton')
    agree_button.pack(pady=5)

def save_api_key_and_restart(new_api_key):
    dotenv_path = find_dotenv() or ".env"
    with open(dotenv_path, "w") as env_file:
        env_file.write(f"OPENAI_API_KEY={new_api_key.strip()}\n")
    restart_app()

def restart_app():
    load_dotenv()
    os.execv(sys.executable, ['python'] + sys.argv)
