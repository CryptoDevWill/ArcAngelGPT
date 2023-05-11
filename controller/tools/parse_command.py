import re
import os
import json

from view.gui.chat_window.current_steps import current_tasks_array
from controller.data.global_variables import thinking, work_mode
from controller.play_sound import play_sound
from view.gui.terminal_window.terminal import Terminal



def parse_command(response: str):
    work_mode.set(True)
    find_json = re.search(r'{(.*?)}', response, re.DOTALL)
    commands = []
    if find_json:
        data = json.loads(find_json.group(0)) # use .group(0) to get the matched string
        print(data)
        if "command" in data:
            os.system(data["command"])
        if "commands" in data:
            for command in data["commands"]:
                os.system(command["command"]) # use command["command"] to execute each command
    else:
        return





def remove_directory(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            remove_directory(item_path)
    os.rmdir(path)


def execute_command():
    tasks = current_tasks_array.get()
    for index, task in enumerate(tasks):
        command_parts = task["command"].split(' ')
        command, args = command_parts[0], command_parts[1:]

        try:
            if command == "mkdir":
                os.mkdir(args[0])
            elif command == "touch":
                with open(args[0], 'a'):
                    os.utime(args[0], None)
            elif command == "echo":
                if ">>" in args:
                    target_file = args[args.index(">>") + 1]
                    content = " ".join(args[:args.index(">>")])
                    with open(target_file, 'a') as file:
                        file.write(f"{content}\n")
                elif ">" in args:
                    target_file = args[args.index(">") + 1]
                    content = " ".join(args[:args.index(">")])
                    with open(target_file, 'w') as file:
                        file.write(f"{content}\n")
                else:
                    print(" ".join(args))
            elif command == "mv":
                destination = args[1] if not os.path.isdir(args[1]) else os.path.join(args[1], os.path.basename(args[0]))
                os.rename(args[0], destination)
            elif command == "rm":
                if "-rf" in args:
                    target_path = args[args.index("-rf") + 1]
                    if os.path.isdir(target_path):
                        remove_directory(target_path)
                    else:
                        print(f"Error: {target_path} is not a directory")
                elif "-r" in args:
                    target_path = args[args.index("-r") + 1]
                    if os.path.isdir(target_path):
                        remove_directory(target_path)
                    else:
                        print(f"Error: {target_path} is not a directory")
                else:
                    os.remove(args[0])
        except Exception as e:
            print(f"Error: {e}")

        tasks[index]["complete"] = True
        current_tasks_array.set(tasks)

    thinking.set(False)
    work_mode.set(False)
    play_sound("complete")
    current_tasks_array.set([])