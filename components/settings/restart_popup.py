# restart.py
import os
import sys
import tkinter as tk
import tkinter.ttk as ttk

def show_restart_popup(master, restart_app):
    restart_popup = tk.Toplevel(master)
    restart_popup.title("Restart Required")
    restart_popup.geometry("300x100")

    restart_message = ttk.Label(restart_popup, text="You must restart the program for changes to take effect.")
    restart_message.pack(pady=10)

    restart_button = ttk.Button(restart_popup, text="RESTART", command=restart_app)
    restart_button.pack(pady=5)

def restart_app():
    os.execv(sys.executable, ['python'] + sys.argv)
