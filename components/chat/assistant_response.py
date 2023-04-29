# assistant_response.py
import openai
import os
from data.conversation import conversation
from dotenv import load_dotenv
from data.global_variables import work_mode
from functions.play_sound import play_sound
from functions.speak import speak
from data.global_variables import loading
from data.global_variables import current_tasks_array, working_directory_path
import os
import re
import json

from functions.execute_command import execute_command
load_dotenv()


# Assitant response
# Assistant response
def assistant_response(chat_window):
    if work_mode.get():
        work_response(chat_window)
    else:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        try:
            conversation.append({
                "role": "system",
                "content": (
                    "AI, please assist me with the following tasks. Whenever I ask for a command execution, "
                    "such as 'make a folder' or 'save the file', provide the command enclosed in backticks (```) "
                    "in your response. This will help trigger the appropriate execution function. "
                    "However, for regular conversations, avoid using backticks so as not to activate "
                    "the execution function inadvertently."
                )
            })
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )
            response = completion.choices[0].message.content
            if '`' in response:
                chat_window.update_conversation()
                play_sound("response")
                work_response(chat_window, response)
            else:
                loading.set(False)
                conversation.append({"role": "assistant", "content": response})
                chat_window.update_conversation()
                play_sound("response")
                # speak(response)
        except openai.error.AuthenticationError as e:
            loading.set(False)
            conversation.append({"role": "assistant", "content": f"Sorry, there was an authentication error. {str(e)}"})
            chat_window.update_conversation()
            play_sound("error")





# Enter work mode
def work_response(chat_window, response):


    prompt = (
        "Process a series of tasks as a headless server environment. "
        "Use autonomous commands like 'echo', 'touch', or 'mv' and avoid any commands that require user interaction. "
        "Please generate an output in the form of an array containing objects with both the "
        "instruction and its corresponding command for each step, as shown in the example below:"
        "Example Output:"
        "["
        "  {'instruction': 'create folder named myfolder', 'command': 'mkdir myfolder'},"
        "  {'instruction': 'create text file called words to that folder', 'command': 'touch myfolder/words.txt'},"
        "  {'instruction': 'add 3 random words to it', 'command': 'echo 'Word1, Word2, Word 3' > myfolder/words.txt'}"
        "]"
        "Ensure that your output strictly adheres to the array format, without any extra characters "
        "or elements that could interfere with the parsing of the next command."
    )


    work_mode.set(True)
    conversation.append({"role": "system", "content": "Entering work mode"})
    chat_window.update_conversation()
    play_sound('work')

    # Ask openai to complete request using Completion Function

    completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=(
                "AI, I need your help in processing a task for a headless server environment. "
                "Use autonomous commands like 'echo', 'touch', or 'mv' and avoid any commands that require "
                "further user engagement, such as 'nano' or 'cd'.\n\n"
                "Here's the instruction I'd like you to follow: make a file called candy\n\n"
                "Please provide an array of objects with the necessary commands for the given instruction, "
                "with the format {\"instruction\": \"...\", \"command\": \"...\", \"complete\": False}, without adding any extra steps."
                f"Here are the instructions I'd like you to follow: " + response + ""
                f"The working directory is given by {working_directory_path}."
            ),
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0,
        )
    task_array = completion.choices[0].text.strip()
    print(task_array)
    # Extract array from task_array using a regular expression
    array_pattern = r'\[[^\]]*\]'
    array_match = re.search(array_pattern, task_array)

    if array_match:
        task_array = array_match.group()
        current_tasks_array.set(task_array)
        try:
            tasks = json.loads(task_array)
            if isinstance(tasks, list) and all(isinstance(task, dict) for task in tasks):
                execute_response(tasks, chat_window)
            else:
                work_mode.set(False)
                loading.set(False)
                raise ValueError("The response is not a valid array.")
        except Exception as e:
            work_mode.set(False)
            loading.set(False)
            print(f"Work mode exited due to error: {e}")
            conversation.append({"role": "system", "content": "Work mode exited due to error."})
            chat_window.update_conversation()
            play_sound("error")
            callback_response(chat_window)
    else:
        work_mode.set(False)
        loading.set(False)
        print("Work mode exited due to error: No array found in the response.")
        conversation.append({"role": "system", "content": "Work mode exited due to error: No array found in the response."})
        chat_window.update_conversation()
        play_sound("error")


# Execute the commands
def execute_response(task_array, chat_window):
    for task in task_array:
        execute_command(task['command'], chat_window)
    # Set work mode false
    work_mode.set(False)
    conversation.append({"role": "system", "content": "Task completed."})
    chat_window.update_conversation()
    play_sound("success")
    callback_response(chat_window)



# Call back response to user
def callback_response(chat_window):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        response = completion.choices[0].message.content
        loading.set(False)
        conversation.append({"role": "assistant", "content": response})
        chat_window.update_conversation()
        play_sound("response")
        # speak(response)    