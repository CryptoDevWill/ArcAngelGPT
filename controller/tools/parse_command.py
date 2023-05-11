import re
import os
import json
import subprocess

from view.gui.chat_window.current_steps import current_tasks_array
from controller.data.global_variables import thinking, work_mode
from controller.play_sound import play_sound
from view.gui.terminal_window.terminal import Terminal



def parse_command(response: str):
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
    if "commands" in data:
        commands = data["commands"]
        command_dicts = [{"step": f"Step {i+1}: {command['description']}", "command": command['command'], "complete": False} for i, command in enumerate(commands)]        
        for command_dict in command_dicts:
            process.append(command_dict["command"])
        current_tasks_array.set(command_dicts)
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
    print(current_tasks_array.get())
    tasks = current_tasks_array.get()
    for index, task in enumerate(tasks):
        command_parts = task["command"].split(' ')
        command = command_parts[0]
        result = subprocess.run(task["command"], shell=True, capture_output=True)
        output = result.stdout.decode()
        tasks[index]["output"] = output
        Terminal.instance().update_output(output)
        tasks[index]["complete"] = True
        current_tasks_array.set(tasks)

    thinking.set(False)
    work_mode.set(False)
    play_sound("complete")
    current_tasks_array.set([])