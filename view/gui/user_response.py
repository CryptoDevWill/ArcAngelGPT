import tkinter as tk
from controller.data.conversation import conversation
from controller.data.global_variables import thinking
from controller.play_sound import play_sound
from controller.components.chat.gpt_response import gpt_response
from controller.components.chat.web_scrape import web_scrape
from view.gui.url_input_module import UrlInput
from view.gui.user_input_module import UserInput
from view.gui.reset_button_module import ResetButtonModule
from model.file_uploads.file_upload import upload_button, upload_response
from controller.data.global_variables import read_mode
import threading


class UserResponse(tk.Frame):  # Inherit from tk.Frame
    def __init__(self, master, chat_window):
        super().__init__(master, bg='#2d2d2d')  # Call the parent class constructor
        self.chat_window = chat_window
        self.max_input_length = 100
        self.char_count = 0
        self.user_frame = tk.Frame(self.master, bg='#2d2d2d')
        self.user_frame.pack(fill='x', padx=10, pady=10)

        # URL input module
        self.url_input_field = UrlInput(self.user_frame)

        # User input module
        self.user_input_field = UserInput(self.user_frame, self.user_response)

        # Reset and back button
        ResetButtonModule(self.user_frame, chat_window)

        #Upload file button
        upload_button(self.user_frame)
        

    def user_response(self, event=None):  # Added event parameter with a default value of None
        user_input = self.user_input_field.user_input.get()
        url_input = self.url_input_field.url_input.get()

        # Append user input
        conversation.append({"role": "user", "content": user_input})
        self.chat_window.update_conversation()
        self.user_input_field.user_input.delete(0, 'end')
        self.url_input_field.url_input.delete(0, 'end')
        play_sound('send')

        # Reject call if still thinking
        if thinking.get():
            conversation.append({"role": "user", "content": "I am thinking, please wait a moment.."})
            self.chat_window.update_conversation()
            play_sound('system')
            return


        # Reject call if no user input
        if not user_input:
            return print("Enter user input")

        # Read more
        if read_mode.get():
            return threading.Thread(target=upload_response, args=(user_input, self.chat_window)).start()

        # Redirect to webscrape if url
        if url_input:
            return threading.Thread(target=web_scrape, args=(url_input, user_input, self.chat_window)).start()

        # GPT response
        if not url_input:
            return threading.Thread(target=gpt_response, args=(user_input, self.chat_window)).start()
