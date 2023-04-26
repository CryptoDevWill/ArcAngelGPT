import tkinter as tk
from components.chat.user_response import UserResponse
from components.chat.chat_window import ChatWindow
from components.terminal.terminal import Terminal


class ChatScreen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        # Create the chat window
        self.chat_window = ChatWindow(self.frame)
        self.chat_window.pack(fill=tk.BOTH, expand=True)

        # Create the user response input field
        UserResponse(self.frame, self.chat_window)

        Terminal.instance(self.master)

    def show(self):
        self.frame.lift()