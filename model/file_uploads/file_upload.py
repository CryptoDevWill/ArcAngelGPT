import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from controller.data.conversation import Conversation
from controller.play_sound import play_sound
from controller.data.global_variables import read_mode, work_mode, thinking
from model.file_uploads.process_chunks import process_chunks
from model.file_uploads.response_chunks import response_chunks
import openai


def open_file(clear_button):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        # print(f"File: {file_path}\nContent:\n{content}")
        read_mode.set(True)
        read_mode.content = content

def clear_read_mode(clear_button):
    read_mode.set(False)

def update_clear_button(clear_button):
    read_mode_status = read_mode.get()
    if read_mode_status:
        clear_button.pack(side=tk.LEFT, padx=(5, 0))
    else:
        clear_button.pack_forget()

def upload_button(parent):
    style = ttk.Style()
    style.configure("Blue.TButton", foreground="#ffffff")
    style.map("Blue.TButton",
              background=[("active", "#0073e6"), ("pressed", "#004799"), ("!disabled", "#0073e6")])
    style.configure("Red.TButton", foreground="#ffffff", background="#ff0000")
    style.configure("TLabel", background="#282a2d", foreground="#aab0b6")

    upload_button = ttk.Button(parent, text="Upload File", style="Blue.TButton", command=lambda: open_file(parent.clear_button))
    upload_button.pack(side=tk.RIGHT, padx=(0, 1))

    parent.clear_button = ttk.Button(parent, text="X", style="Red.TButton", width=1, command=lambda: clear_read_mode(parent.clear_button))
    # Don't pack the clear_button here, it will be packed when read_mode is set to True

    read_mode.set_callback(lambda: update_clear_button(parent.clear_button))

def upload_response(user_input, chat_window):
    conversation = Conversation.instance()
    content = read_mode.content
    read_mode.set(False)
    work_mode.set(True)
    thinking.set(True)
    try:
        chunks = process_chunks(user_input, content)
        response = response_chunks(chunks, chat_window)
        conversation.append({"role": "assistant", "content": response})
        play_sound("response")
    except openai.error.InvalidRequestError as e:
        error_message = "Error: " + str(e)
        conversation.append({"role": "assistant", "content": error_message})
        play_sound("error")
    except openai.error.AuthenticationError as e:
        error_message = "Error: " + str(e)
        conversation.append({"role": "assistant", "content": error_message})
        play_sound("error")
    finally:
        work_mode.set(False)
        thinking.set(False)
        chat_window.update_conversation()
