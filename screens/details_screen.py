import os
import tkinter as tk
from dotenv import load_dotenv
from functions.speak import mute_button

load_dotenv()

class DetailsScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        self.api_key = os.getenv('OPENAI_API_KEY')
        masked_api_key = self.mask_api_key(self.api_key)
        self.api_key_label = tk.Label(self.frame, text=f"OPENAI API KEY: {masked_api_key}")
        self.api_key_label.pack(pady=10)

        # Create a mute button
        self.mute_button = tk.Button(self.frame, text="Mute Speech", command=self.toggle_mute)
        self.mute_button.pack(pady=10)

        # Set the initial mute state to False
        self.mute_speech = False

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
