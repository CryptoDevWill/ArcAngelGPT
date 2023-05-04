import tkinter as tk
from data.conversation import conversation
from data.global_variables import thinking
from functions.play_sound import play_sound
from components.chat.gpt_response import gpt_response
from components.chat.web_scrape import web_scrape
from components.chat.url_input_module import UrlInput
from components.chat.user_input_module import UserInput
from components.chat.reset_button_module import ResetButtonModule
import threading


class UserResponse:
    def __init__(self, master, chat_window):
        self.master = master
        self.chat_window = chat_window
        self.max_input_length = 100
        self.char_count = 0
        self.user_frame = tk.Frame(self.master, bg='#2d2d2d')
        self.user_frame.pack(fill='x', padx=10, pady=10)

        # URL input module
        self.url_input_field = UrlInput(self.user_frame)

        # User input module
        self.user_input_field = UserInput(self.user_frame, self.user_response)

        # Create and place the reset button
        reset_button = ResetButtonModule(self.user_frame, chat_window)

    def user_response(self, event=None):  # Added event parameter with a default value of None
        # Reject call if still thinking
        if thinking.get():
            return print("please wait")

        user_input = self.user_input_field.user_input.get()
        url_input = self.url_input_field.url_input.get()

        # Reject call if no user input
        if not user_input:
            return print("Enter user input")

        # Append user input
        conversation.append({"role": "user", "content": user_input})
        self.chat_window.update_conversation()
        self.user_input_field.user_input.delete(0, 'end')
        self.url_input_field.url_input.delete(0, 'end')
        play_sound('send')

        # Redirect to webscrape if url
        if url_input:
            return threading.Thread(target=web_scrape, args=(url_input, user_input, self.chat_window)).start()

        # GPT response
        if not url_input:
            return threading.Thread(target=gpt_response, args=(user_input, self.chat_window)).start()

