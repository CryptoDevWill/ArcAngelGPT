from dotenv import load_dotenv
from data.global_variables import username, working_directory
from functions.get_file_tree import get_file_tree
from utils.get_current_time_date import get_current_time_date
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
    f"The current time is {time}. "
    f"The current date is {date}. "
    f"Your working directory is {working_directory}. "
    f"Your assigned user is {username}. "
    f"These are the files and folders in your working directory {get_file_tree()}"
    "using only 'mkdir', 'touch', or 'echo', provide the commands needed to execute each task individually in the working_directory. Example ``` mkdir folder ```, ``` touch file.txt ```, ``` echo 'Hello,' > folder/file.txt"
)}



conversation = [initial_system_prompt]
