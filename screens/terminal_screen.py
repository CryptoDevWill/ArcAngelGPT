import os
import tkinter as tk
from dotenv import load_dotenv

load_dotenv()

class TerminalScreen:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True)

    def show(self):
        self.frame.lift()

# Create a Tkinter window and display the DetailsScreen
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry('500x300')
#     root.title('Termianl Output')
#     details_screen = TerminalScreen(root)
#     details_screen.show()
#     root.mainloop()
