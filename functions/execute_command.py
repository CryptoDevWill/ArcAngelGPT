import subprocess
import shlex
from gui.terminal import Terminal
from data.conversation import conversation

FORBIDDEN_COMMANDS = ["cd", "nano"]

def update_terminal_output(terminal, output):
    if terminal is not None:
        terminal.update_output(output + '\n')

def is_command_forbidden(command):
    for forbidden_command in FORBIDDEN_COMMANDS:
        if forbidden_command in command.split():
            return True
    return False

def execute_command(command, chat_window):
    # Check if command is forbidden
    if is_command_forbidden(command):
        forbidden_message = f"Error: '{command}' is a forbidden command."
        conversation.append({"role": "system", "content": forbidden_message})
        chat_window.update_conversation()
        return forbidden_message

    # Output to terminal
    terminal = Terminal.instance()
    update_terminal_output(terminal, f"Executing command: " + command)
    conversation.append({"role": "system", "content": f"Executing command: {command}"})
    chat_window.update_conversation()

    try:
        # Run the command in a shell environment
        process = subprocess.run(command, text=True, capture_output=True, check=True, shell=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        # Output to terminal
        error_message = f"Error: '{command}' is not a valid command."
        update_terminal_output(terminal, error_message)
        update_terminal_output(terminal, str(e))

        # Append the error message to the conversation as a system message
        conversation.append({"role": "system", "content": error_message})
        chat_window.update_conversation()
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
            if output:
                conversation.append({"role": "system", "content": output})

            conversation.append({"role": "system", "content": success_message})
            chat_window.update_conversation()
            return success_message
