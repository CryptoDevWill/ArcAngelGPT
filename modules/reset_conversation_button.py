from tkinter import ttk
from data.global_variables import username, working_directory
from functions.get_file_tree import get_file_tree
from utils.get_current_time_date import get_current_time_date
from data.conversation import conversation, initial_system_prompt

time, date = get_current_time_date()

def reset(chat_window):
    print("Reset button clicked!")
    conversation.clear()  # Clear the entire conversation
    conversation.append(initial_system_prompt)  # Add the initial_system_prompt back to the conversation
    chat_window.update_conversation()  # Update the chat window to reflect the reset conversation

def reset_conversation_button(parent, chat_window):
    button = ttk.Button(parent, text="Reset", style="blue.TButton", command=lambda: reset(chat_window))
    chat_window.update_conversation()

    return button
