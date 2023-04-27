# assistant_response.py
import openai
import os
from data.conversation import conversation
from dotenv import load_dotenv
from data.global_variables import work_mode
from functions.play_sound import play_sound
from functions.speak import speak
from data.global_variables import loading
import os
import re
import json

from functions.execute_command import execute_command
load_dotenv()


# Assitant response
def assistant_response(chat_window):
    work_mode.get()
    if work_mode.get():
        work_response(chat_window)
    else:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response = completion.choices[0].message.content
        if '`' in response:
            conversation.append({"role": "assistant", "content": "Okay i'll start working on that now!"})
            chat_window.update_conversation()
            play_sound("response")
            work_response(chat_window, response)
        else:
            loading.set(False)
            conversation.append({"role": "assistant", "content": response})
            chat_window.update_conversation()
            play_sound("response")
            speak(response)



# Enter work mode
def work_response(chat_window, response):
    working_directory_path = os.getcwd()
    prompt = ('Your current working directory is ' + working_directory_path + '. '
            'You are an autonomous terminal AI that only outputs an array string of ALL the steps needed to complete the instructions in order. '
            'You are to order each step based on its correct order in the command chain. For example, "touch" will come before "echo" if writing to the same file. '
            'Use only the following commands: "touch", "mkdir", "rm", and "echo". Construct file paths to achieve the desired outcome without changing directories, opening files, or directly editing files. '
            '### Example Output: [{"instruction": "create folder named myfolder", "command": "mkdir myfolder"}, {"instruction": "create json file called jokes", "command": "touch jokes.json"}]. '
            '### Here are the instructions: ' + response)
    
    work_mode.set(True)
    conversation.append({"role": "system", "content": "Entering work mode"})
    chat_window.update_conversation()
    play_sound('work')

    # Ask openai to complete request using Completion Function
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
                execute_response(tasks, chat_window)
            else:
                raise ValueError("The response is not a valid array.")
        except Exception as e:
            work_mode.set(False)
            print(f"Work mode exited due to error: {e}")
            conversation.append({"role": "system", "content": "Work mode exited due to error."})
            chat_window.update_conversation()
            play_sound("error")
    else:
        work_mode.set(False)
        print("Work mode exited due to error: No array found in the response.")
        conversation.append({"role": "system", "content": "Work mode exited due to error: No array found in the response."})
        chat_window.update_conversation()
        play_sound("error")


# Execute the commands
def execute_response(task_array, chat_window):
    for task in task_array:
        execute_command(task['command'], chat_window)
    work_mode.set(False)
    conversation.append({"role": "system", "content": "Task complete!"})
    chat_window.update_conversation()
    play_sound("success")
    work_mode.set(False)  # Add this line to ensure work_mode is updated to False
    assistant_response(chat_window)