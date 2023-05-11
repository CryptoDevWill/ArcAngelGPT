import tkinter as tk
from controller.data.conversation import Conversation
from controller.data.global_variables import thinking
from controller.play_sound import play_sound
from controller.tools.parse_command import parse_command
from controller.components.file_tree.get_file_tree import get_file_tree
import threading
import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_response(user_input, chat_window):
    conversation = Conversation.instance()
    try:
        thinking.set(True)
        conversation_length = len(conversation)
        conversation.append({"role": "system", "content": (
                                f"Your file tree is {get_file_tree()}. The Operating system is {os.name}, "
                                f"so please only include commands that are compatible with my OS.\n"
                                f"The user should not be expected to use STDIN or STDOUT.\n"
                                f"If it is simple you can just use answer, but if a command is needed, use command.\n"
                                f"You must use the following structure, using command or answer:\n"
                                f"{{\n"
                                f"    \"commands\": [\n"
                                f"        {{\n"
                                f"            \"command\": \"command to execute\",\n"
                                f"            \"answer\": \"answer to a question, or no json possible\"\n"
                                f"            \"description\": \"description of command\"\n"
                                f"        }}\n"
                                f"    ],\n"
                                f"}}"
                                f"Do not use more than one json response in a single message."
                                )})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation.get())
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


