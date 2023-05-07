import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def open_file(label):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        print(f"File: {file_path}\nContent:\n{content}")
        label.config(text="File read!", foreground="#aab0b6")

def upload_button(parent):
    style = ttk.Style()
    style.configure("TButton", background="#30475e", foreground="#ffffff")
    style.configure("TLabel", background="#282a2d", foreground="#aab0b6")

    upload_button = ttk.Button(parent, text="Upload File", command=lambda: open_file(parent.upload_status_label))
    upload_button.pack(side=tk.LEFT, padx=(0, 10))
    parent.upload_status_label = ttk.Label(parent, text="")
    parent.upload_status_label.pack(side=tk.LEFT, fill=tk.BOTH)
