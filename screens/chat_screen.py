import tkinter as tk
from components.chat.user_response import UserResponse
from components.chat.chat_window import ChatWindow
from components.terminal.terminal import Terminal


class ChatScreen:
    def __init__(self, master):
        self.master = master

        # create a container frame for the chat window and user input field
        self.container = tk.Frame(self.master, bg='#f5f5f5', padx=10, pady=10)
        self.container.pack(fill='both', expand=True)

        # create the chat window
        self.chat_window = ChatWindow(self.container, bg='#ffffff', bd=1, relief='solid')
        self.chat_window.pack(fill='both', expand=True, padx=10, pady=10)

        # create the user response input field
        self.user_input = UserResponse(self.container, self.chat_window)
        
        # set focus to the user input field by default
        self.user_input.user_input.focus()





    def show(self):
        self.container.pack(fill='both', expand=True)
        self.user_input.user_input.focus()