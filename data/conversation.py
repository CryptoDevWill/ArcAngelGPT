import os
from dotenv import load_dotenv
from data.global_variables import username, working_directory
from functions.get_file_tree import get_file_tree
from utils.get_current_time_date import get_current_time_date
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
    f"The current time is {time}. "
    f"The current date is {date}. "
    f"The current type of Operating System is {os.name}."
    f"Your working directory is {working_directory} this path has alredy been set and should be used at all times. "
    f"Your assigned user is {username}. "
    f"These are the files and folders in your working directory {get_file_tree()}"
)}



conversation = [initial_system_prompt]
