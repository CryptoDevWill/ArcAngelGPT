import os
from dotenv import load_dotenv
from data.global_variables import username
from utils.get_current_time_date import get_current_time_date
import sys
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
    f"The current time is {time}. "
    f"The current date is {date}. "
    f"Your Python version is {sys.version}"
    f"Your assigned user is {username}."
)}



conversation = [initial_system_prompt]
