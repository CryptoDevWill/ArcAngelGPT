import tkinter as tk
from components.chat.user_response import UserResponse
from components.chat.chat_window import ChatWindow
from gui.terminal import Terminal
from functions._init import _init

class ChatScreen:
    def __init__(self, master):
        self.master = master

        # create a container frame for the chat window and user input field
        self.container = tk.Frame(self.master, bg='#2d2d2d', padx=10, pady=10)
        self.container.pack(fill='both', expand=True)

        # create the chat window
        self.chat_window = ChatWindow(self.container, bg='#1e1e1e', bd=1, relief='solid')
        self.chat_window.pack(fill='both', expand=True, padx=10, pady=10)

        # create the user response input field
        self.user_input = UserResponse(self.container, self.chat_window)
        self.user_input.user_input.configure(bg='#1e1e1e', fg='white', insertbackground='white')

        # set focus to the user input field by default
        self.user_input.user_input.focus()

        #Send initial system message to ChatGPT with a 1-second delay
        self.master.after(1000, lambda: _init(self.chat_window))

    def show(self):
        self.container.pack(fill='both', expand=True)
        self.user_input.user_input.focus()
