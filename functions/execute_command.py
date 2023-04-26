import subprocess
import shlex
from components.terminal.terminal import Terminal
from data.global_variables import conversation

def execute_command(command):
    # Command execution
    cmd_args = shlex.split(command)

    # Output to terminal
    terminal = Terminal.instance()
    if terminal is not None:
        terminal.update_output(f"Executing command: {command}\n")

    try:
        process = subprocess.run(cmd_args, text=True, capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        error_message = f"Error: '{command}' is not a valid command."
        if terminal is not None:
            terminal.update_output(error_message + '\n')
            terminal.update_output(str(e) + '\n')
    else:
        # Output to terminal
        if terminal is not None:
            output = process.stdout if process.returncode == 0 else process.stderr
            terminal.update_output(output)

        # Check if the process completed successfully
        if process.returncode == 0:
            if terminal is not None:
                terminal.update_output("Process completed successfully.\n")
