import tkinter as tk
from tkinter import ttk
from screens.chat_screen import ChatScreen
from screens.details_screen import DetailsScreen

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Arc Angel Ai")

        # Create a Notebook widget
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)

        # Chat Tab
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Chat")
        self.chat = ChatScreen(self.tab1)
        self.chat.show()

        # Details Tab
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Details")
        self.details = DetailsScreen(self.tab2)
        self.details.show()


