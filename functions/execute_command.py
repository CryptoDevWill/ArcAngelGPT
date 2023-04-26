import subprocess
import shlex
from components.terminal.terminal import Terminal

def execute_command(command):
    # Command execution
    cmd_args = shlex.split(command)

    # Output to terminal
    terminal = Terminal.instance()
    if terminal is not None:
        terminal.update_output(f"Executing command: {command}\n")

    process = subprocess.run(cmd_args, text=True, capture_output=True)

    # Output to terminal
    if terminal is not None:
        output = process.stdout if process.returncode == 0 else process.stderr
        terminal.update_output(output)

    # Check if the process completed successfully
    if process.returncode == 0:
        if terminal is not None:
            terminal.update_output("Process completed successfully.\n")
    else:
        if terminal is not None:
            terminal.update_output(f"Process completed with error (return code {process.returncode}).\n")
