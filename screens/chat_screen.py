import tkinter as tk
from components.chat.user_response import UserResponse
from components.chat.chat_window import ChatWindow
from gui.current_steps import create_steps_box
from gui.thinking_indicator import ThinkingIndicator
from components.file_tree.file_tree import FileTree
from modules.work_mode_label import WorkModeLabel


class ChatScreen:
    def __init__(self, master):
        self.master = master
        self.master.config(bg="#2d2d2d") # set background color of master widget

        label = WorkModeLabel(self.master)
        label.pack()

        # create a container frame for the chat window and user input field
        self.container = tk.Frame(self.master, bg='#2d2d2d', padx=10, pady=10)
        self.container.pack(fill='both', expand=True)

        # create left and right side panes
        self.left_pane = tk.Frame(self.container, bg='#2d2d2d')
        self.right_pane = tk.Frame(self.container, bg='#2d2d2d')

        self.left_pane.pack(side='left', fill='both', expand=True)
        self.right_pane.pack(side='right', fill='y', expand=False)

        # create the chat window
        self.chat_window = ChatWindow(self.left_pane, bg='#1e1e1e', bd=1, relief='solid')
        self.chat_window.pack(fill='both', expand=True, padx=10, pady=10)

        # create the user response input field
        self.user_input = UserResponse(self.left_pane, self.chat_window)
        self.user_input.user_input_field.user_input.configure(bg='#1e1e1e', fg='white', insertbackground='white')

        # Loading indicator
        self.loading_indicator = ThinkingIndicator(self.left_pane, bg='#2d2d2d', fg='white')
        self.loading_indicator.pack(side='bottom', padx=10, pady=10)

        # set focus to the user input field by default
        self.user_input.user_input_field.user_input.focus()

        # create the file tree
        self.file_tree = FileTree(self.right_pane, bg='#2d2d2d')
        self.file_tree.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # create the current steps box
        steps_box = create_steps_box(self.right_pane)
        steps_box.pack(side='top', padx=10, pady=10)

        # #Send initial system message to ChatGPT with a 1-second delay
        # self.master.after(500, lambda: _init(self.chat_window))

    def show(self):
        self.container.pack(fill='both', expand=True)
        self.user_input.user_input_field.user_input.focus()
