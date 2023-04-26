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

        # Create a PanedWindow widget with no border
        self.paned_window = tk.PanedWindow(self.frame, orient=tk.VERTICAL, sashrelief='raised', sashwidth=8, bd=0)
        self.paned_window.pack(fill='both', expand=True)

        # Create a dummy frame for the upper part of the PanedWindow
        self.dummy_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.dummy_frame, stretch='always')

        # Change the fg color to old-school green and add the Text widget to the PanedWindow
        self.text_widget = tk.Text(self.paned_window, wrap='word', bg='black', fg='#009d09', height=4, highlightthickness=0)
        self.paned_window.add(self.text_widget)
        self.text_widget.config(state=tk.DISABLED)

        # Set the initial height of the terminal to 4 lines
        self.frame.update()
        font = tkfont.Font(font=self.text_widget['font'])
        terminal_height = font.metrics('linespace') * 4
        self.paned_window.sash_place(0, 0, self.frame.winfo_height() - terminal_height)
        
    def show(self):
        self.frame.lift()

    def update_output(self, stdout):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, stdout)
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)
