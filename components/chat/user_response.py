import threading
import tkinter as tk
from data.conversation import conversation
from components.chat.assistant_response import assistant_response
from functions.play_sound import play_sound
class UserResponse:
    def __init__(self, master, chat_window):
        self.master = master
        self.chat_window = chat_window

        self.user_input = tk.Entry(
            self.master,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#cccccc',
            font=('Helvetica', 12),
            fg='#333333',
            bg='#f5f5f5',
            relief='flat',
        )
        self.user_input.pack(fill='x', padx=10, pady=10)

        # add a placeholder text
        self.user_input.insert(0, 'Enter your text here...')

        # add focus and unfocus styling
        def on_focus(event):
            self.user_input.delete(0, 'end')
            self.user_input.config(fg='#333333')
            self.user_input.config(bg='#ffffff')

        def on_unfocus(event):
            if not self.user_input.get():
                self.user_input.insert(0, 'Enter your text here...')
                self.user_input.config(fg='#bbbbbb')
                self.user_input.config(bg='#f5f5f5')

        self.user_input.bind('<FocusIn>', on_focus)
        self.user_input.bind('<FocusOut>', on_unfocus)
        self.user_input.bind('<Return>', self.user_response)
    def user_response(self, event):
        input_text = self.user_input.get()
        conversation.append({"role": "user", "content": input_text})
        self.chat_window.update_conversation()
        self.user_input.delete(0, 'end')
        play_sound('send')
        # Run assistant_response() in a separate thread
        threading.Thread(target=self.run_assistant_response).start()

    def run_assistant_response(self):
        assistant_response(self.chat_window)
