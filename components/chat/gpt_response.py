import tkinter as tk
from data.conversation import conversation
from data.global_variables import thinking
from functions.play_sound import play_sound
from tools.parse_command import parse_command
from components.file_tree.get_file_tree import get_file_tree
import threading
import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_response(user_input, chat_window):
    try:
        thinking.set(True)
        conversation_length = len(conversation)
        conversation.append({"role": "system", "content": f"Your file tree is {get_file_tree()}Translate human text into non-interactive executable terminal command prompts. Only give one command, do not give multiple examples. Enclose each response in triple back ticks. I do not want any advice or notes or anything that cannot be directly copied and pasted into a terminal session. You are to act like a computer in this regard."})
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


