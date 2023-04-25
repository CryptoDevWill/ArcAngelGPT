# openai_chat.py
import openai
import os
import re
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

commands = ["mkdir", "touch"]

# Chat conversation
def ChatGPT(conversation):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response = completion.choices[0].message.content
        conversation.append({ "role": "assistant", "content": response })

        result = None
        for command in commands:
            regex = rf'{command} (\S+)'
            match = re.search(regex, response)
            if match:
                argument = match.group(1)
                if command == "mkdir":
                    result = _mkdir(argument)
                elif command == "touch":
                    result = _touch(argument)
                break

        if result:
            conversation.append({ "role": "assistant", "content": result })

        return "Task complete"
    except openai.error.AuthenticationError as e:
        error_message = str(e)
        print(f"Error: {error_message}")
        return error_message

def _mkdir(directory_name):
    exit_code = os.system(f'mkdir {directory_name}')
    if exit_code == 0:
        return f"Directory '{directory_name}' has been created successfully."
    else:
        return f"Error creating directory '{directory_name}': {os.strerror(exit_code)}"

def _touch(file_name):
    exit_code = os.system(f"touch {file_name}")
    if exit_code == 0:
        return f"File '{file_name}' has been created successfully."
    else:
        return f"Error creating file '{file_name}': {os.strerror(exit_code)}"
