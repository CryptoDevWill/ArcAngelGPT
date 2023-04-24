# chat_submit.py
from dotenv import load_dotenv
from programs.chatgpt import ChatGPT
import os
import platform
import subprocess

load_dotenv()

working_directory_path = os.getcwd()

# Get files and folders in the working directory
files_and_folders = os.system("ls")
home_dir = os.path.expanduser("~")
username = os.getlogin()

def list_files_as_tree():
    def get_tree(startpath):
        exclude = set(['.git', '__pycache__'])  # Exclude .git and __pycache__ directories
        
        tree = ''
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if d not in exclude]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            tree += f"{indent}{os.path.basename(root)}/"
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                tree += f"{subindent}{file}"
        return tree

    # Get the current working directory and list its files and folders as a tree
    cwd = os.getcwd()
    files_and_folders_tree = get_tree(cwd)
    
    return files_and_folders_tree



file_tree = list_files_as_tree()


conversation = [
            {
                "role": "system",
                "content": "You are an AI computer server assistant. " + 
                "Your username is " + username +
                ". Your home directory is " + home_dir +
                ". Your working directory is " + working_directory_path +
                ". The files and folders in your working directory are " + file_tree
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
