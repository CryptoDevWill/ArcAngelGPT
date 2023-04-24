import tkinter as tk
from components.chat.chat_window import ChatWindow

class ChatScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        self.chat_box = ChatWindow(self.frame)
        
    def show(self):
        self.frame.lift()
