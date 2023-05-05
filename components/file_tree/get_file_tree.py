import os
from colorama import init, Fore, Style

def get_file_tree():
    init(autoreset=True)  # Automatically reset color after each print

    working_dir = os.getcwd()

    tree_lines = []
    tree_tags = []

    # Define color codes
    GREY = "folder"
    BLUE = "python_file"
    ORANGE = "js_file"
    YELLOW = "file"
    RESET = ""

    exclude_folders = ["assets", "components", "data", "functions", "gui", "dist", "build", "openai", "tools", "user_scripts", "utils", "screens", "__pycache__", "modules", "main.py"]
    exclude_files = ["LICENSE", "requirements.txt", "README.md", "run", "_main.py", "main.spec" ]

    for name in os.listdir(working_dir):
        if name.startswith('.'):  # skip hidden files and folders
            continue
        if name in exclude_folders or name in exclude_files:
            continue
        path = os.path.join(working_dir, name)
        if os.path.isdir(path):
            tree_lines.append(f"{name}")
            tree_tags.append((GREY, path))
            for subname in os.listdir(path):
                if not subname.startswith('.'):
                    color = RESET
                    if subname.endswith('.py'):
                        color = BLUE
                    elif subname.endswith('.js'):
                        color = "js_file"
                    tree_lines.append(f" - {subname}")
                    tree_tags.append((color, os.path.join(path, subname)))
        else:
            color = RESET
            if name.endswith('.py'):
                color = BLUE
            elif name.endswith('.js'):
                color = "js_file"
            tree_lines.append(f"{name}")
            tree_tags.append((color, os.path.join(working_dir, name)))

    return tree_lines, tree_tags
