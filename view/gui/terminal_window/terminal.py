import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk

from base import Instance


class Terminal(metaclass=Instance):

    def __init__(self, master=None):
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        # Create the Text widget
        self.text_widget = tk.Text(self.frame, wrap='word', bg='black', fg='#009d09', height=4, highlightthickness=0)
        self.text_widget.pack(fill='both', expand=True)
        self.text_widget.config(state=tk.DISABLED)

    def show(self):
        self.frame.lift()

    def update_output(self, stdout):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, stdout)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)
