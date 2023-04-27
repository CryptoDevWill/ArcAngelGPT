import os
import tkinter as tk
from dotenv import load_dotenv
from functions.speak import mute_button
from data.global_variables import *

load_dotenv()

class DetailsScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)
        self.api_key = os.getenv('OPENAI_API_KEY')
        masked_api_key = self.mask_api_key(self.api_key)
        self.api_key_label = tk.Label(self.frame, text=f"OPENAI API KEY: {masked_api_key}")
        self.api_key_label.pack(pady=10)
        self.api_key_label = tk.Label(self.frame, text=f"Working Directory: {os.getcwd()}")
        self.api_key_label.pack(pady=10)
        self.api_key_label = tk.Label(self.frame, text=f"Operating System: {platform.system()} {platform.release()}")
        self.api_key_label.pack(pady=10)
        self.api_key_label = tk.Label(self.frame, text=f"Architecture: {platform.machine()}")
        self.api_key_label.pack(pady=10)
        self.api_key_label = tk.Label(self.frame, text=f"Processor: {platform.processor()}")
        self.api_key_label.pack(pady=10)
        memory = psutil.virtual_memory().total / (1024 * 1024 * 1024)
        disk_usage = psutil.disk_usage('/').total / (1024 * 1024 * 1024)
        self.api_key_label = tk.Label(self.frame, text=f"Memory: {memory:.2f}")
        self.api_key_label.pack(pady=10)
        self.api_key_label = tk.Label(self.frame, text=f"Disk Usage: {disk_usage:.2f}")
        self.api_key_label.pack(pady=10)



    def mask_api_key(self, api_key):
        if api_key:
            half_length = len(api_key) // 2
            return api_key[:half_length] + '*' * (len(api_key) - half_length)
        return None

    def show(self):
        self.frame.lift()

    def toggle_mute(self):
        self.mute_speech = not self.mute_speech
        if self.mute_speech:
            mute_button(True)
            self.mute_button.config(text="Unmute Speech")
        else:
            mute_button(False)
            self.mute_button.config(text="Mute Speech")

# Create a Tkinter window and display the DetailsScreen
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.title('API Key Display')
    details_screen = DetailsScreen(root)
    details_screen.show()
    details_screen.speak("Hello, world!")
    root.mainloop()
