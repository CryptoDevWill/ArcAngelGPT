from tkinter import ttk, Frame
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

def remove_latest_message(chat_window):
    print("Back button clicked!")
    if len(conversation) > 1:  # Ensure there is a message to remove
        conversation.pop(-1)  # Remove the latest message from the conversation
        chat_window.update_conversation()  # Update the chat window to reflect the updated conversation

def reset_conversation_button(parent, chat_window):
    button_frame = Frame(parent)
    
    reset_button = ttk.Button(button_frame, text="Reset", command=lambda: reset(chat_window))
    reset_button.pack(side='right', padx=(0, 5))

    back_button = ttk.Button(button_frame, text="Back", command=lambda: remove_latest_message(chat_window))
    back_button.pack(side='right')

    chat_window.update_conversation()

    return button_frame
