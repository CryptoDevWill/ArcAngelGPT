import tkinter as tk
from controller.data.conversation import conversation
from controller.data.global_variables import thinking
from controller.play_sound import play_sound
from controller.tools.parse_command import parse_command
from controller.components.file_tree.get_file_tree import get_file_tree
import threading
import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_response(user_input, chat_window):
    try:
        thinking.set(True)
        conversation_length = len(conversation)
        conversation.append({"role": "system", "content": (
                                f"Your file tree is {get_file_tree()}. The Operating system is {os.name}."
                                )})
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


