# assistant_response.py
import openai
import os
from data.conversation import conversation
from dotenv import load_dotenv
from data.global_variables import work_mode
import os
import re
import json

from functions.execute_command import execute_command
load_dotenv()

def assistant_response(chat_window):
    if work_mode.get():
        work_response(chat_window)
    else:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response = completion.choices[0].message.content
        print(response)
        if '`' in response:
            work_mode.set(True)
            work_response(chat_window, response)
        else:
            print(response)
            conversation.append({"role": "assistant", "content": response})
            chat_window.update_conversation()


def work_response(chat_window, response):
    working_directory_path = os.getcwd()
    prompt = ('Your current working directory is ' + working_directory_path + '. '
            'You are an autonomous terminal AI that only outputs an array string of ALL the steps needed to complete the instructions in order. '
            'Do not use "cd", "open", "nano", or "save" commands, as you cannot change directories, open files, or directly edit files. '
            'Construct file paths to achieve the desired outcome. '
            '### Example Output: [{"instruction": "create folder named myfolder", "command": "mkdir myfolder"}, {"instruction": "create json file called jokes", "command": "touch jokes.json"}]. '
            '### Here are the instructions: ' + response)

    chat_window.update_conversation()
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0
        )
    task_array = completion.choices[0].text.strip()
    print(task_array)
    # Extract array from task_array using a regular expression
    array_pattern = r'\[[^\]]*\]'
    array_match = re.search(array_pattern, task_array)

    if array_match:
        task_array = array_match.group()

        try:
            tasks = json.loads(task_array)
            if isinstance(tasks, list) and all(isinstance(task, dict) for task in tasks):
                execute_response(tasks)
            else:
                raise ValueError("The response is not a valid array.")
        except Exception as e:
            print(f"Work mode exited due to error: {e}")
            conversation.append({"role": "assistant", "content": "Work mode exited due to error."})
            work_mode.set(False)
            chat_window.update_conversation()
    else:
        print("Work mode exited due to error: No array found in the response.")
        conversation.append({"role": "assistant", "content": "Work mode exited due to error: No array found in the response."})
        work_mode.set(False)
        chat_window.update_conversation()

def execute_response(task_array):
    work_mode.set(False)
    for task in task_array:
        execute_command(task['command'])