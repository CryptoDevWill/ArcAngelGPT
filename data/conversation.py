import os
from dotenv import load_dotenv
from data.global_variables import username, working_directory
from components.file_tree.get_file_tree import get_file_tree
from utils.get_current_time_date import get_current_time_date
import sys
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
    f"The current time is {time}. "
    f"The current date is {date}. "
    f"Your Python version is {sys.version}"
    f"Your assigned user is {username}. "
    f"These are the files and folders {get_file_tree()}"
)}



conversation = [initial_system_prompt]
