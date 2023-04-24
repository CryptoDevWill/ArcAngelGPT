# chat_window.py
import tkinter as tk
from tkinter import ttk
from components.chat.chat_send import user_response
import os
import platform
import subprocess


directory_path = os.getcwd()

# Get files and folders in the working directory
result = subprocess.run(["ls"], capture_output=True, text=True)
files_and_folders = result.stdout.strip()

class ChatWindow:
    def __init__(self, master):
        self.master = master
        self.chat_window = tk.Text(master, wrap='word', bd=0, bg='#1b1d1c', fg='#f5f5f5', font=('Helvetica', 15))
        self.chat_window.pack(side='top', fill='both', expand=True)
        self.chat_window.configure(state='disabled')

        self.chat_window.tag_configure('user', background='#141414', spacing1=10, spacing2=10, spacing3=10)
        self.chat_window.tag_configure('assistant', background='#2b2b2b', spacing1=10, spacing2=10, spacing3=10)


        frame = tk.Frame(master, padx=5, pady=5)
        frame.pack(side='bottom', fill='x')

        # Textfield input
        input_field = tk.Text(frame, height=2, bd=0, bg='#1b1d1c', highlightthickness=0, font=('Helvetica', 15), pady=5, padx=5)
        input_field.pack(side='left', fill='x', expand=True)

        # Send button
        submit_button = ttk.Button(frame, text="Send", style="C.TButton", command=lambda: user_response(input_field, self.chat_window, self.master, self.conversation))
        submit_button.pack(side='right')

    conversation = [
            {
                "role": "system",
                "content": "You are an AI assistant that can execute command-line terminal prompts. "
                "This is your directory path: " + directory_path
                + "\n\nThese are the files and folders in your working directory:\n" + files_and_folders
                + "\n\nThese are your system details: os.name - " + os.name + ", platform.system() - " + platform.system(),
            }
        ]