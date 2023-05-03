import re
from gui.current_steps import current_tasks_array
from data.global_variables import thinking
from data.global_variables import work_mode
from functions.play_sound import play_sound
import time
import os
from components.chat.chat_window import ChatWindow
import subprocess
from gui.terminal import Terminal

def parse_command(response: str):
    if '```' not in response:
        print("No commands found.")
        return
    work_mode.set(True)
    chat_window = ChatWindow()  # Instantiate ChatWindow
    chat_window.update_conversation()
    allowed_commands = ["mkdir", "touch", "echo", "rm", "mv", "cat", "python", "node"]
    pattern = r'```(.*?)```'
    command_blocks = re.findall(pattern, response, re.DOTALL)
    
    commands = []
    for block in command_blocks:
        block_commands = block.strip().split('\n')
        for cmd in block_commands:
            cmd = cmd.strip()
            if any(cmd.startswith(allowed_cmd) for allowed_cmd in allowed_commands):
                commands.append(cmd)

    command_dicts = [{"step": f"Step {i+1}: {cmd}", "command": cmd, "complete": False} for i, cmd in enumerate(commands)]
    current_tasks_array.set(command_dicts)
    print(current_tasks_array.get())
    execute_command()



# must_have = "ArcAngelGPT/working_directory"

def execute_command():
    print("execute command")
    tasks = current_tasks_array.get()
    terminal_instance = Terminal.instance()  # Get the Terminal instance
    for index, task in enumerate(tasks):
        task_string = task["command"]
    
    
        try:
            result = subprocess.run(task_string, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)  # Capture command output
            output = result.stdout + result.stderr  # Combine stdout and stderr
        except subprocess.CalledProcessError as e:
            output = e.stderr  # Print the error message
        terminal_instance.update_output(output)  # Update the Terminal output
        tasks[index]["complete"] = True
        current_tasks_array.set(tasks)  # Set the current_tasks_array after each iteration
        play_sound("task_complete")
        # time.sleep(1)  # Delay for 3 seconds after each iteration

    thinking.set(False)
    work_mode.set(False)
    play_sound("complete")
    current_tasks_array.set([])



