import subprocess
import shlex
from components.terminal.terminal import Terminal
from data.global_variables import conversation

def update_terminal_output(terminal, output):
    if terminal is not None:
        terminal.update_output(output + '\n')

def execute_command(command):
    # Command execution
    cmd_args = shlex.split(command)

    # Output to terminal
    terminal = Terminal.instance()
    update_terminal_output(terminal, f"Executing command: " + command)
    conversation.append({"role": "system", "content": f"Executing command: {command}"})

    try:
        process = subprocess.run(cmd_args, text=True, capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        # Output to terminal
        error_message = f"Error: '{command}' is not a valid command."
        update_terminal_output(terminal, error_message)
        update_terminal_output(terminal, str(e))

        # Append the error message to the conversation as a system message
        conversation.append({"role": "system", "content": error_message})
        return error_message
    else:
        # Output to terminal
        output = process.stdout if process.returncode == 0 else process.stderr
        update_terminal_output(terminal, output)

        # Check if the process completed successfully
        if process.returncode == 0:
            # Output to terminal
            success_message = f"Command {command} executed successfully."
            update_terminal_output(terminal, success_message)

            # Append the successful command message to the conversation as a system message
            conversation.append({"role": "system", "content": success_message})
            return success_message
