import os
from data.global_variables import work_mode
from functions.play_sound import play_sound

allowed_commands = [ "mkdir" ]

def parse_command(text):
    # Find object between the triple backticks
    start = text.find("```")
    if start == -1:
        return None
    end = text.find("```", start + 3)
    if end == -1:
        return None

    # Extract the command
    command_line = text[start+3:end].strip()
    parts = command_line.split()
    if len(parts) < 2:
        return None

    command = parts[0]
    folder = parts[1]

    # Check if the command is allowed
    if command not in allowed_commands:
        return None

    # Start work mode
    work_mode.set(True)
    play_sound("work")
    # Execute the command
    os.system(f"{command} working_directory/{folder}")
    work_mode.set(False)