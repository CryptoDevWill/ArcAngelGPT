import tkinter as tk
from data.global_variables import conversation
from functions.execute_command import execute_command
class UserResponse:
    def __init__(self, master):
        self.master = master

        self.user_input = tk.Entry(self.master, borderwidth=0, highlightthickness=0)
        self.user_input.pack(fill='x', padx=10, pady=10)
        self.user_input.bind('<Return>', self.user_response)

    def user_response(self, event):
        input_text = self.user_input.get()
        execute_command(input_text)
        response = {"role": "user", "content": input_text}
        conversation.append(response)
        print(conversation)
        self.user_input.delete(0, 'end')
