import tkinter as tk
from tkinter import ttk

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
        master.title("ArcAngelAi")
        master.geometry("950x700")
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)