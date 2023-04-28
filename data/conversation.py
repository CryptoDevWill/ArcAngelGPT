from dotenv import load_dotenv
import os
import platform
import psutil


load_dotenv()

working_directory_path = os.getcwd()

operating_system = platform.system() + " " + platform.release()
architecture = platform.machine()
processor = platform.processor()
memory = psutil.virtual_memory().total / (1024 * 1024 * 1024)
disk_usage = psutil.disk_usage('/').total / (1024 * 1024 * 1024)

# Get files and folders in the working directory
files_and_folders = os.system("ls")
home_dir = os.path.expanduser("~")
try:
    username = os.environ['USERNAME']
except:
    username = os.environ['USER']

def list_files_as_tree():
    def get_tree(startpath):
        exclude = set(['.git', '__pycache__'])  # Exclude .git and __pycache__ directories
        
        tree = ''
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if d not in exclude]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            tree += f"{indent}{os.path.basename(root)}/"
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                tree += f"{subindent}{file}"
        return tree

    # Get the current working directory and list its files and folders as a tree
    cwd = os.getcwd()
    files_and_folders_tree = get_tree(cwd)
    
    return files_and_folders_tree



file_tree = list_files_as_tree()


conversation = [
    {
        "role": "system",
        "content": "You are an AI computer server assistant. " + 
        "Your name is " + username +
        ". Your home directory is " + home_dir +
        ". Your working directory is " + working_directory_path +
        # ". The files and folders in your working directory are " + file_tree +
        # ". Your operating system is " + operating_system +
        # ". Your system architecture is " + architecture +
        # ". Your processor is " + processor +
        # f". You have {memory:.2f} GB of RAM and {disk_usage:.2f} GB of total disk space." +
        " Your primary task is to help break down projects into tasks and execute terminal commands to complete them. Your responses are short and precise"
    }
]
