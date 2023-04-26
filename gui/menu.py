import tkinter as tk
from tkinter import ttk
from screens.chat_screen import ChatScreen
from screens.details_screen import DetailsScreen
from screens.output_screen import OutputScreen

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("Arc Angel GPT")

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

        # Details Tab
        self.tab3 = tk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Output")
        self.details = OutputScreen(self.tab3)
        self.details.show()


