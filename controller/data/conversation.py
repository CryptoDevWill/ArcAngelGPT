import os
from dotenv import load_dotenv
from controller.data.global_variables import username
from controller.utils.get_current_time_date import get_current_time_date
import sys
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
f"Hello {username}, you are now interacting with a Linux-based AI model. "
"Please provide a single command or instruction for each interaction. "
"The AI will respond with non-interactive terminal commands only, enclosed in triple backticks ``` for clarity. "
"These commands are designed to be executed and completed in a headless environment, without any explanatory text. "
)}



conversation = [initial_system_prompt]
