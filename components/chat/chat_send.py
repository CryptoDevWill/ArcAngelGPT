# chat_submit.py
from dotenv import load_dotenv
from programs.chatgpt import ChatGPT
import os
import platform
import subprocess

load_dotenv()

directory_path = os.getcwd()

# Get files and folders in the working directory
result = subprocess.run(["ls"], capture_output=True, text=True)
files_and_folders = result.stdout.strip()

home_dir = os.path.expanduser("~")
print(home_dir)

username = os.getlogin()
print(username)


conversation = [
            {
                "role": "system",
                "content": "You are an AI assistant that can execute command-line terminal prompts. "
                "This is your directory path: " + directory_path
                + "\n\nThese are the files and folders in your working directory:\n" + files_and_folders
                + "\n\nThese are your system details: os.name - " + os.name + ", platform.system() - " + platform.system(),
            }
        ]


def user_response(input_field, chat_window, master):
    prompt = input_field.get('1.0', 'end-1c')
    user_message = {"role": "user", "content": prompt}
    conversation.append(user_message)

    chat_window.configure(state='normal')
    chat_window.insert('end', "User: " + user_message['content'] + "\n", 'user')
    chat_window.configure(state='disabled')
    chat_window.see('end')
    input_field.delete('1.0', 'end')
    master.after(100, assistant_response, chat_window)


def assistant_response(chat_window):    

    completion = ChatGPT(conversation)

    chat_window.configure(state='normal')
    chat_window.insert('end', "Assistant: " + completion + "\n", 'assistant')
    chat_window.configure(state='disabled')
    chat_window.see('end')
