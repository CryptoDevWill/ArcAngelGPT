import os
import tkinter as tk
from dotenv import load_dotenv

load_dotenv()

class OutputScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        self.api_key_label = tk.Label(self.frame, text=f"hello")
        self.api_key_label.pack(pady=10)

    def show(self):
        self.frame.lift()

# Create a Tkinter window and display the DetailsScreen
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.title('Termianl Output')
    details_screen = OutputScreen(root)
    details_screen.show()
    root.mainloop()
