import tkinter as tk
from tkinter import ttk

class DialogScreen(ttk.Frame):
    def __init__(self, master=None, api_function=None, **kwargs):
        super().__init__(master, **kwargs)
        self.api_function = api_function

        style = ttk.Style()
        style.configure('Dark.TLabel', background='#2b2b2b', foreground='#ffffff')
        style.configure('Dark.TEntry', background='#333333', foreground='#ffffff', fieldbackground='#333333', insertcolor='#ffffff')

        self.label_var = tk.StringVar()
        self.label_var.set("Waiting for input...")
        self.api_response_label = ttk.Label(self, textvariable=self.label_var, style='Dark.TLabel', wraplength=400)
        self.api_response_label.pack(pady=20)

        self.user_input = ttk.Entry(self, width=50, style='Dark.TEntry')
        self.user_input.pack(pady=10)
        self.user_input.bind("<Return>", self.on_user_input)
        self.user_input.focus_set()

    def on_user_input(self, event):
        user_text = self.user_input.get()
        self.user_input.delete(0, tk.END)
        if self.api_function:
            api_response = self.api_function(user_text)
            self.label_var.set(api_response)
        else:
            self.label_var.set("API function not provided.")

    def show(self):
        self.pack(expand=True, fill=tk.BOTH)
