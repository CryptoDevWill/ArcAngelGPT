from tkinter import ttk, Frame
from data.conversation import conversation, initial_system_prompt


def reset(chat_window):
    print("Reset button clicked!")
    conversation.clear()
    conversation.append(initial_system_prompt)
    chat_window.update_conversation()

def remove_latest_message(chat_window):
    print("Back button clicked!")
    if len(conversation) > 1:
        conversation.pop(-1)
        chat_window.update_conversation()

class ResetButtonModule(Frame):  # Renamed class
    def __init__(self, parent, chat_window):
        super().__init__(parent)

        reset_button = ttk.Button(self, text="Reset", command=lambda: reset(chat_window))
        reset_button.pack(side='right', padx=(0, 5))

        back_button = ttk.Button(self, text="Back", command=lambda: remove_latest_message(chat_window))
        back_button.pack(side='right')

        chat_window.update_conversation()

        self.pack(side='right')
