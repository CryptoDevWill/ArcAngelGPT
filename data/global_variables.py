from dotenv import load_dotenv
import os
import platform
import psutil

load_dotenv()

global working_directory_path
working_directory_path = os.getcwd()

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



class WorkMode:
    def __init__(self):
        self.value = False

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

work_mode = WorkMode()

class ExecuteMode:
    def __init__(self):
        self.value = False

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

execute_mode = ExecuteMode()


class Loading:
    def __init__(self):
        self.value = False

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

loading = Loading()



class CurrentTasksArray:
    def __init__(self):
        self.value = []

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

current_tasks_array = CurrentTasksArray()
