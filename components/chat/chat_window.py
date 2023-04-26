import tkinter as tk
from tkinter import ttk
from components.chat.user_response import user_response

class ChatWindow:
    def __init__(self, master):
        self.master = master
        self.chat_window = tk.Text(master, wrap='word', bd=0, bg='#1b1d1c', fg='#f5f5f5', font=('Helvetica', 15))
        self.chat_window.pack(side='top', fill='both', expand=True)
        self.chat_window.configure(state='disabled')

        self.chat_window.tag_configure('user', background='#141414', spacing1=10, spacing2=10, spacing3=10)
        self.chat_window.tag_configure('assistant', background='#2b2b2b', spacing1=10, spacing2=10, spacing3=10)

        frame = tk.Frame(master, padx=5, pady=5)
        frame.pack(side='bottom', fill='x')

        # Textfield input
        input_field = tk.Text(frame, height=1, bd=0, bg='#1b1d1c', highlightthickness=0, font=('Helvetica', 15), fg='#ffffff', pady=5, padx=5)
        input_field.pack(side='left', fill='x', expand=True)

        # Function to check if input field is empty
        def is_input_empty(input_field):
            return len(input_field.get('1.0', 'end-1c').strip()) == 0

        # Modified function to handle Return key event
        def on_return_key(event):
            if not is_input_empty(input_field):
                user_response(input_field, self.chat_window, self.master)
            return 'break'

        # Send button
        submit_button = ttk.Button(frame, text="Send", style="C.TButton", command=lambda: on_return_key(None))
        submit_button.pack(side='right')

        # Bind the Return key to the input_field
        input_field.bind('<Return>', on_return_key)
