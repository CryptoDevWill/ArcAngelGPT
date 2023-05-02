from dotenv import load_dotenv
import os
import platform
import psutil
from functions.play_sound import play_sound

load_dotenv()

try:
    username = os.environ['USERNAME']
except:
    username = os.environ['USER']

global root_directory_path
root_directory_path = os.getcwd()

global working_directory
working_directory = os.getcwd() + "/working_directory"

global operating_system
operating_system = platform.system() + " " + platform.release()

global architecture
architecture = platform.machine()

global processor
processor = platform.processor()

global memory
memory = psutil.virtual_memory().total / (1024 * 1024 * 1024)

global disk_usage
disk_usage = psutil.disk_usage('/').total / (1024 * 1024 * 1024)

global files_and_folders
files_and_folders = os.system("ls")

global home_dir
home_dir = os.path.expanduser("~")


global forbbiden_commands
forbidden_commands = "cd, nano, vi, vim, save, open, code"



class WorkMode:
    def __init__(self):
        self.value = False
        self.callbacks = []

    def set(self, state):
        if state == True:
            play_sound('work') # Call the play_sound() function with argument 'work'
        self.value = state
        for callback in self.callbacks:
            callback()

    def get(self):
        return self.value

    def set_callback(self, callback):
        self.callbacks.append(callback)

work_mode = WorkMode()


class Thinking:
    def __init__(self):
        self.value = False

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

thinking = Thinking()



class Loading:
    def __init__(self):
        self.value = False

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

loading = Loading()

