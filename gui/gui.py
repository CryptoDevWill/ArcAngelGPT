import tkinter as tk
from tkinter import ttk
import sys
import os

def _resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(sys.argv[0]), relative_path)

class GUI:
    def __init__(self, master):
        self.master = master

        # Set the style
        style = ttk.Style()
        style.theme_create("custom", parent="alt", settings={
            "TNotebook": {"configure": {"background": "#2d2d2d", "foreground": "white"}},
            "TNotebook.Tab": {
                "configure": {"background": "#2d2d2d", "foreground": "white", "padding": [15, 5]},
                "map": {"background": [("selected", "#1e1e1e")],
                        "foreground": [("selected", "white")],
                        "expand": [("selected", [1, 1, 1, 0])]}},
            "TFrame": {"configure": {"background": "#2d2d2d"}},
            "TLabel": {"configure": {"background": "#2d2d2d", "foreground": "white"}},
            "TButton": {"configure": {"background": "#1e1e1e", "foreground": "white"}},
            "TEntry": {"configure": {"background": "#1e1e1e", "foreground": "white"}},
            "TCheckbutton": {"configure": {"background": "#2d2d2d", "foreground": "white"}},
            "TRadiobutton": {"configure": {"background": "#2d2d2d", "foreground": "white"}},
            "TCombobox": {"configure": {"background": "#1e1e1e", "foreground": "white"}},
            "TScrollbar": {"configure": {"background": "#2d2d2d", "troughcolor": "#1e1e1e"}},
        })

        style.theme_use("custom")

        # Create the widgets
        master.title("ArcAngelAI")
        master.geometry("950x600")
        # Set the window icon
        icon_path = _resource_path("assets/images/icon.ico")
        master.iconbitmap(icon_path)
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)