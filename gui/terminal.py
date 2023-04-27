import tkinter as tk
import tkinter.font as tkfont

class Terminal:
    _instance = None

    @classmethod
    def instance(cls, master=None):
        if cls._instance is None and master is not None:
            cls._instance = cls(master)
        return cls._instance

    def __init__(self, master):
        if Terminal._instance is not None:
            raise RuntimeError("Only one instance of Terminal is allowed.")
        self.frame = tk.Frame(master)
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
