import os
from dotenv import load_dotenv
from controller.data.global_variables import username
from controller.utils.get_current_time_date import get_current_time_date
import sys
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
f"Hello {username}, Create a json that describes the commands needed to perform the following tasks:\n"
)}



conversation = [initial_system_prompt]
