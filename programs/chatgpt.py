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
        if response:
            pattern = r"```python\n(.*?)```"
            match = re.search(pattern, response, re.DOTALL)
            if match:
                code_block = match.group(1)
                function_pattern = r"def\s+(\w+)\("
                function_match = re.search(function_pattern, code_block)
                print(function_match)
                if function_match:
                    function_name = function_match.group(1)
                    file_name = f"{function_name}.py"
                    save_code_block(code_block, file_name)
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
            else:
                return response
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
def save_code_block(code_block, file_name):
    function_pattern = r"def\s+(\w+)\("
    function_match = re.search(function_pattern, code_block)
    if function_match:
        function_name = function_match.group(1)
        save_dir = "./user_scripts"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_path = os.path.join(save_dir, file_name)
        with open(file_path, "w") as f:
            f.write(code_block)
            print(f"Code block saved to {file_path}")