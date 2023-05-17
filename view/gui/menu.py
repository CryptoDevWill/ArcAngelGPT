import tkinter as tk
from tkinter import ttk
from view.gui.chat_window.chat_screen import ChatScreen
from view.gui.details_window.details_screen import DetailsScreen
from view.gui.terminal_window.terminal_screen import TerminalScreen
from view.gui.settings_window.settings_screen import SettingsScreen

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("ArcAngelAI V2 (beta) 2.0.2")

        # Set menu bar background color
        self.master.config(bg='#2d2d2d')

        # Create a Notebook widget
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)

        # Chat Tab
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Chat")
        self.chat = ChatScreen(self.tab1)
        self.chat.show()

        # Terminal Tab
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Terminal")
        self.details = TerminalScreen(self.tab2)
        self.details.show()

        # Details Tab
        self.tab3 = tk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Details")
        self.details = DetailsScreen(self.tab3)
        self.details.show()

        # settings Tab
        self.tab4 = tk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Settings")
        self.details = SettingsScreen(self.tab4)
        self.details.show()

        
