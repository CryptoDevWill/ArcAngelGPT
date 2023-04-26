import tkinter as tk
from data.conversation import conversation
from functions.execute_command import execute_command
from components.chat.assistant_response import assistant_response


class UserResponse:
    def __init__(self, master):
        self.master = master

        self.user_input = tk.Entry(self.master, borderwidth=0, highlightthickness=0)
        self.user_input.pack(fill='x', padx=10, pady=10)
        self.user_input.bind('<Return>', self.user_response)

    def user_response(self, event):
        input_text = self.user_input.get()
        conversation.append({"role": "user", "content": input_text})
        assistant_response()
        self.user_input.delete(0, 'end')
