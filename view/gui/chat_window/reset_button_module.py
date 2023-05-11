from tkinter import ttk, Frame
from controller.data.conversation import Conversation

def reset(chat_window):
    print("Reset button clicked!")
    Conversation.instance().reset()
    # conversation.clear()
    # conversation.append(initial_system_prompt)
    chat_window.update_conversation()

def remove_latest_message(chat_window):
    print("Back button clicked!")
    # if len(conversation) > 1:
    #     conversation.pop(-1)
    if Conversation.instance().undo():
        chat_window.update_conversation()

class ResetButtonModule(Frame):
    def __init__(self, parent, chat_window):
        super().__init__(parent)

        style = ttk.Style()
        style.configure("BurntOrange.TButton", foreground="#ffffff", background="#cc5500")
        style.map("BurntOrange.TButton", background=[("active", "#cc5500"), ("pressed", "#cc5500"), ("!disabled", "#cc5500")])

        reset_button = ttk.Button(self, text="Reset", command=lambda: reset(chat_window), style="BurntOrange.TButton")
        reset_button.pack(side='right', padx=(0, 5))

        back_button = ttk.Button(self, text="Back", command=lambda: remove_latest_message(chat_window), style="BurntOrange.TButton")
        back_button.pack(side='right')

        chat_window.update_conversation()

        self.pack(side='right')
