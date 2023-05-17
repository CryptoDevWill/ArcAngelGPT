import os
import tkinter as tk
from dotenv import load_dotenv
from view.gui.terminal_window.terminal import Terminal  # Import the Terminal class

load_dotenv()


class TerminalScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)
        self.terminal = Terminal(self.frame)  # Create a Terminal instance

    def show(self):
        self.frame.lift()
        self.terminal.show()  # Show the Terminal instance
