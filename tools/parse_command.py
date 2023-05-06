import re
import os
import subprocess

from gui.current_steps import current_tasks_array
from data.global_variables import thinking, work_mode
from functions.play_sound import play_sound
from gui.terminal import Terminal

def parse_command(response: str):
    if '```' not in response:
        print("No commands found.")
        return
    work_mode.set(True)

    allowed_commands_unix = ["mkdir", "touch", "echo"]
    allowed_commands_windows = ["mkdir", "echo"]
    allowed_commands = allowed_commands_unix if os.name == 'posix' else allowed_commands_windows

    pattern = r'```(.*?)```'
    command_blocks = re.findall(pattern, response, re.DOTALL)

    commands = []
    for block in command_blocks:
        block_commands = block.strip().split('\n')
        for cmd in block_commands:
            cmd = cmd.strip()
            if any(cmd.startswith(allowed_cmd) for allowed_cmd in allowed_commands):
                cmd = convert_to_cmd_command(cmd)
                commands.append(cmd)

    command_dicts = [{"step": f"Step {i+1}: {cmd}", "command": cmd, "complete": False} for i, cmd in enumerate(commands)]
    current_tasks_array.set(command_dicts)
    execute_command()

def convert_to_cmd_command(command: str):
    if os.name != 'posix' and command.startswith("touch"):
        file_name = command.split(" ")[1]
        return f"echo. > {file_name}"
    else:
        return command

def execute_command():
    tasks = current_tasks_array.get()
    terminal_instance = Terminal.instance()
    is_posix = os.name == 'posix'

    for index, task in enumerate(tasks):
        task_string = task["command"]

        if not is_posix:
            task_string = convert_to_cmd_command(task_string)

        try:
            result = subprocess.run(task_string, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            output = result.stdout + result.stderr
        except subprocess.CalledProcessError as e:
            output = e.stderr
        terminal_instance.update_output(output)
        tasks[index]["complete"] = True
        current_tasks_array.set(tasks)
        play_sound("task_complete")

    thinking.set(False)
    work_mode.set(False)
    play_sound("complete")
    current_tasks_array.set([])
