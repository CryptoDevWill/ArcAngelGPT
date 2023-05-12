import re
import os
import json
import subprocess
from view.gui.chat_window.chat_window import ChatWindow

from view.gui.chat_window.current_steps import CurrentTasksArray
from controller import WorkMode, Thinking, Conversation
from controller.play_sound import play_sound
from view.gui.terminal_window import Terminal


def parse_command(response: str):
    work_mode = WorkMode()
    work_mode.set(True)
    start_delim = '{'
    end_delim = '}'
    try:
        start_index = response.index(start_delim)
        end_index = response.rindex(end_delim) + len(end_delim)
    except ValueError:
        print(f"Error: could not find start or end delimiter in response: {response}")
        work_mode.set(False)
        return

    json_str = response[start_index:end_index]
    if not json_str:
        print(f"Error: extracted JSON string is empty in response: {response}")
        work_mode.set(False)
        return
    
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        print(f"Error: failed to parse JSON in response: {response}")
        work_mode.set(False)
        return
    process = []
    Terminal().update_output(data)
    if "commands" in data:
        if "answer" in data['commands'][0]:
            answer = data['commands'][0]['answer']
            Terminal().update_output(answer + "\n")
            conversation = Conversation()
            conversation.append({"role": "assistant", "content": answer})
            ChatWindow().update_conversation()
            work_mode.set(False)
            return
        if "command" in data['commands'][0]:
            commands = data["commands"]
            command_dicts = [{"step": f"Step {i+1}: {command['description']}", "command": command['command'], "complete": False} for i, command in enumerate(commands)]        
            for command_dict in command_dicts:
                process.append(command_dict["command"])
            CurrentTasksArray().set(command_dicts)
            execute_command()
    work_mode.set(False)


def remove_directory(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            remove_directory(item_path)
    os.rmdir(path)


def execute_command():
    current_tasks_array = CurrentTasksArray()
    print(current_tasks_array.get())
    tasks = current_tasks_array.get()
    for index, task in enumerate(tasks):
        command_parts = task["command"].split(' ')
        #attempt to fix stupid newlines in windows.
        if command_parts[0] == "echo":
            task["command"] = re.sub(r"(?m)^echo", "printf", task["command"])
        result = subprocess.run(task["command"], shell=True, capture_output=True)
        output = result.stdout.decode()
        Terminal().update_output(task["command"] + "\n")
        tasks[index]["output"] = output
        Terminal().update_output(output + "\n")
        tasks[index]["complete"] = True
        Terminal().update_output(f"Step {index+1} complete \n")
        current_tasks_array.set(tasks)

    Thinking().set(False)
    WorkMode().set(False)
    play_sound("complete")
    current_tasks_array.set([])