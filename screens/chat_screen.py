import tkinter as tk
from functions.execute_command import execute_command
from components.terminal.terminal import Terminal
from components.chat.user_response import UserResponse

class ChatScreen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        UserResponse(self.frame)

        Terminal.instance(self.master)
        
    def show(self):
        self.frame.lift()
