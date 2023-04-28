import os
import tkinter as tk
import tkinter.ttk as ttk
import platform
import psutil

class DetailsScreen:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.pack(fill='both', expand=True)

        self.details_labels = [
            f"Working Directory: {os.getcwd()}",
            f"Operating System: {platform.system()} {platform.release()}",
            f"Architecture: {platform.machine()}",
            f"Processor: {platform.processor()}",
            f"Memory: {psutil.virtual_memory().total / (1024 * 1024 * 1024):.2f} GB",
            f"Disk Usage: {psutil.disk_usage('/').total / (1024 * 1024 * 1024):.2f} GB"
        ]

        for detail in self.details_labels:
            label = ttk.Label(self.frame, text=detail)
            label.pack(pady=10)

    def show(self):
        self.frame.lift()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x350')
    root.title('System Details')
    root.configure(bg='#2c2f33')  # Set the background color to match the dark theme

    # Configure ttk styles
    style = ttk.Style()
    style.configure('TLabel', background='#2c2f33', foreground='#ffffff')

    details_screen = DetailsScreen(root)
    root.mainloop()
