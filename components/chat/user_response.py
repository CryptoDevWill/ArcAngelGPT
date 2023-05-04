import tkinter as tk
from data.conversation import conversation
from data.global_variables import thinking, files_and_folders
from functions.play_sound import play_sound
from tools.parse_command import parse_command
from components.chat.gpt_response import gpt_response
import threading
import os
import openai
from modules.reset_conversation_button import reset_conversation_button

# Added import
from tkinter import Entry

openai.api_key = os.getenv("OPENAI_API_KEY")

class UserResponse:
    def __init__(self, master, chat_window):
        self.master = master
        self.chat_window = chat_window
        self.max_input_length = 100
        self.char_count = 0
        self.user_frame = tk.Frame(self.master, bg='#2d2d2d')
        self.user_frame.pack(fill='x', padx=10, pady=10)

        # Added URL Entry field
        self.url_input = Entry(
            self.user_frame,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#cccccc',
            font=('Helvetica', 14),
            fg='white',
            bg='#000000',
            relief='flat',
            insertbackground='white'
        )
        self.url_input.pack(side='top', fill='x', expand=True, pady=(0, 5))

        # Add placeholder text for the URL input field
        self.url_input.insert(0, 'URL')
        self.url_input.config(fg='#bbbbbb')

        self.user_input = tk.Entry(
            self.user_frame,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#cccccc',
            font=('Helvetica', 16),
            fg='white',
            bg='#2d2d2d',
            relief='flat',
            insertbackground='white',
            validate='key',
            validatecommand=(self.master.register(self.validate_input), '%P')
        )
        self.user_input.pack(side='left', fill='x', expand=True)
        # Create and place the reset button
        reset_button = reset_conversation_button(self.user_frame, chat_window)
        reset_button.pack(side='right')

        # add a placeholder text
        self.user_input.insert(0, 'Enter your text here...')
        self.user_input.config(fg='#bbbbbb')

        # add focus and unfocus styling
        def on_focus(event):
            self.user_input.delete(0, 'end')
            self.user_input.config(fg='white')
            self.user_input.config(bg='#1e1e1e')

        def on_unfocus(event):
            if not self.user_input.get():
                self.user_input.insert(0, 'Enter your text here...')
                self.user_input.config(fg='#bbbbbb')
                self.user_input.config(bg='#2d2d2d')

        self.user_input.bind('<FocusIn>', on_focus)
        self.user_input.bind('<FocusOut>', on_unfocus)
        
        # Modified binding for Return key
        self.user_input.bind('<Return>', lambda event: self.fire_function_before_response())

        # add character counter
        self.char_counter = tk.Label(
            self.user_frame,
            text=f'0/{self.max_input_length}',
            font=('Helvetica', 14),
            fg='#999999',
            bg='#2d2d2d'
        )
        self.char_counter.pack(side='right', padx=(0, 10))

        # bind key events to update character counter
        self.user_input.bind('<KeyRelease>', self.update_char_counter)

    def validate_input(self, input_text):
        return len(input_text) <= self.max_input_length

    def update_char_counter(self, event):
        input_text = self.user_input.get()
        self.char_count = len(input_text)
        self.char_counter.config(text=f'{self.char_count}/{self.max_input_length}')
        if self.char_count == self.max_input_length:
            self.char_counter.config(fg='#a10000')
        else:
            self.char_counter.config(fg='#999999')

    def fire_function_before_response(self):
        # Add your function call here before calling user_response
        # example_function()

        # Print input from the add_url_entry field
        url_input = self.url_input.get()
        print("URL input:", url_input)

        self.user_response()

    def user_response(self):
        if thinking.get():
            return print("please wait")
        else:
            user_input = self.user_input.get()
            if not user_input:
                return  # exit function if user input is empty
            conversation.append({"role": "user", "content": user_input})
            self.chat_window.update_conversation()
            print(conversation)
            self.user_input.delete(0, 'end')
            play_sound('send')
            # Execute Arc in a separate thread
            gpt_thread = threading.Thread(target=gpt_response, args=(user_input, self.chat_window))
            gpt_thread.start()



