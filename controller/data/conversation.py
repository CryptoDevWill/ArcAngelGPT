import os
from dotenv import load_dotenv
from controller.data.global_variables import username
from controller.utils.get_current_time_date import get_current_time_date
import sys
load_dotenv()

time, date = get_current_time_date()

initial_system_prompt = {"role": "system", "content": (
f"You are ChatGPT-Json. For each input from the user, create a json that describes the commands needed to perform the given task.\n"
)}


class Conversation:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if Conversation._instance is not None:
            raise RuntimeError("Only one instance of Conversation is allowed.")
        self.chat = [initial_system_prompt]

    def __getitem__(self, item):
        return self.chat[item]

    def __len__(self):
        return len(self.chat)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError(f"Key must be int, not {type(key)}")
        if isinstance(value, dict) and len(value) == 2 and "role" in value and "content" in value:
            self.chat[key] = value
        else:
            raise ValueError(f"Invalid message format for dict {value}")

    def append(self, item):
        if isinstance(item, dict) and len(item) == 2 and "role" in item and "content" in item:
            self.chat.append(item)
        else:
            raise ValueError(f"Invalid message format for dict {item}")

    def clear(self):
        self.chat.clear()

    def clear_role(self, role):
        for i in range(len(self.chat)):
            if self[i]["role"] == role:
                self.pop(i)

    def get(self):
        return self.chat

    def pop(self, value):
        self.chat.pop(value)

    def reset(self):
        self.chat = [initial_system_prompt]

    def undo(self):
        if len(self) > 1:
            return self.pop(-1)
        return None
