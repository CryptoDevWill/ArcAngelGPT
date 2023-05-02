import tkinter as tk
from data.conversation import conversation
from data.global_variables import thinking
from gui.current_steps import current_tasks_array
from functions.play_sound import play_sound
from tools.parse_command import parse_command
import threading
import os
import openai
from arcangelai import Arc
from data.global_variables import work_mode

arc = Arc({"key": "abc123", "name": "Arc"})
openai.api_key = os.getenv("OPENAI_API_KEY")


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
        if thinking.get():
            return print("please wait")
        else:
            user_input = self.user_input.get()
            if not user_input:
                return # exit function if user input is empty
            conversation.append({"role": "user", "content": user_input})
            self.chat_window.update_conversation()
            self.user_input.delete(0, 'end')
            play_sound('send')
            # Execute Arc in a separate thread
            gpt_thread = threading.Thread(target=gpt_response, args=(user_input, self.chat_window))
            gpt_thread.start()


def gpt_response(user_input, chat_window):
    try:
        thinking.set(True)
        conversation_length = len(conversation)
        conversation.append({"role": "system", "content": "If the user is asking to execute commands then using only 'mkdir', 'touch', 'echo', 'rm', or 'mv', provide one set of commands needed to execute each task individually with no human interaction using absolute paths only NO 'cd'. Example ``` mkdir folder ```, ``` touch file.txt ```, ``` echo 'Hello,' > folder/file.txt."})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
        conversation.pop(conversation_length)
        chat_response = completion.choices[0].message
        conversation.append({"role": "assistant", "content": chat_response.content})

        if chat_response:
            command = threading.Thread(target=parse_command, args=(chat_response.content,))
            command.start()

    except openai.error.InvalidRequestError as e:
        error_message = "Error: " + str(e)
        conversation.append({"role": "assistant", "content": error_message})
        thinking.set(False)
    except openai.error.AuthenticationError as e:
        error_message = "Error: " + str(e)
        conversation.append({"role": "assistant", "content": error_message})
        thinking.set(False)
    finally:
        chat_window.update_conversation()
        play_sound("response")
        thinking.set(False)


