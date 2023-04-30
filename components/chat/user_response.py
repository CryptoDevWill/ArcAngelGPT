import tkinter as tk
from data.conversation import conversation
from functions.play_sound import play_sound
from arcangelai import Arc
import threading

arc = Arc({"key": "abc123", "name": "Will" })

class UserResponse:
    def __init__(self, master, chat_window):
        self.master = master
        self.chat_window = chat_window
        self.max_input_length = 100
        self.char_count = 0
        self.user_frame = tk.Frame(self.master, bg='#2d2d2d')
        self.user_frame.pack(fill='x', padx=10, pady=10)

        self.user_input = tk.Entry(
            self.user_frame,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#cccccc',
            font=('Helvetica', 14),
            fg='white',
            bg='#2d2d2d',
            relief='flat',
            insertbackground='white',
            validate='key',
            validatecommand=(self.master.register(self.validate_input), '%P')
        )
        self.user_input.pack(side='left', fill='x', expand=True)

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
        self.user_input.bind('<Return>', self.user_response)

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

    def user_response(self, event):
        user_input = self.user_input.get()
        conversation.append({"role": "user", "content": user_input})
        self.chat_window.update_conversation()
        self.user_input.delete(0, 'end')
        play_sound('send')
        # Execute Arc in a separate thread
        arc_thread = threading.Thread(target=arc_response, args=(user_input, self.chat_window))
        arc_thread.start()


def arc_response(user_input, chat_window):

    response = arc.chat(user_input)
    print(response['message'])
    if response['code'] == 200:
        if response['message'] == 'command':
            conversation.append({"role": "assistant", "content": response['message']})
            chat_window.update_conversation()
            play_sound("response")
            return

        if response['message'] == 'question':
            conversation.append({"role": "assistant", "content": response['message']})
            chat_window.update_conversation()
            play_sound("response")
            return
    else:
            print(response.message)
            conversation.append({"role": "assistant", "content": response['message']})
            chat_window.update_conversation()
            play_sound("response")
            return
