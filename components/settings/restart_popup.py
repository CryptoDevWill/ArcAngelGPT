# restart.py
import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from dotenv import load_dotenv

def show_restart_popup(master, restart_app):
    restart_popup = tk.Toplevel(master)
    restart_popup.title("Restart Required")
    restart_popup.geometry("400x100")
    restart_popup.configure(bg='#2c2f33')

    style = ttk.Style()
    style.configure('TLabel', background='#2c2f33', foreground='#ffffff')
    style.configure('TButton', background='#43b581', foreground='#ffffff', bordercolor='#43b581')
    style.map('TButton', background=[('active', '#3aa76d'), ('pressed', '#3aa76d')])

    restart_message = ttk.Label(restart_popup, text="You must restart the program for changes to take effect.", style='TLabel')
    restart_message.pack(pady=10)

    restart_button = ttk.Button(restart_popup, text="RESTART", command=restart_app, style='TButton')
    restart_button.pack(pady=5)

def restart_app():
    load_dotenv()  # Add this line to reload the environment variables
    os.execv(sys.executable, ['python'] + sys.argv)
