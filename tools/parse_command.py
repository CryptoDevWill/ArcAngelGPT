import os
from data.global_variables import work_mode
from functions.play_sound import play_sound

allowed_commands = [ "mkdir", "touch", "echo" ]

def parse_command(text):
    # Find object between the triple backticks
    start = text.find("```")
    if start == -1:
        return None
    end = text.find("```", start + 3)
    if end == -1:
        return None

    play_sound("work")
    # Extract the command
    command_line = text[start+3:end].strip()
    parts = command_line.split()
    if len(parts) < 2:
        work_mode.set(False)
        return play_sound("error")

    command = parts[0]
    folder = parts[1]

    # Check if the command is allowed
    if command not in allowed_commands:
        work_mode.set(False)
        print(command + " not allowed")
        return play_sound("error")

    # Start work mode
    work_mode.set(True)
    # Execute the command
    os.system(f"{command} working_directory/{folder}")
    play_sound("success")
    work_mode.set(False)