import tkinter as tk
from gui.gui import GUI
from gui.menu import Menu
import time
from PIL import Image, ImageTk


class ArcAngelGPT:
    def __init__(self):
        self.window = tk.Tk()
        self.show_loading_screen()
        GUI(self.window)
        Menu(self.window)
        self.window.mainloop()

    def show_loading_screen(self):
        self.window.withdraw()  # Hide the main window

        # Create and display the loading window
        loading_window = tk.Toplevel(self.window)
        loading_window.overrideredirect(True)  # Remove window borders
        loading_window.geometry("700x400")  # Adjust the size of the loading window as needed

        # Load the spinning image and display it
        # Replace "path/to/spinning_image.gif" with the path to your image
        spinning_image = Image.open("assets/images/load_screen.png")
        spinning_image = ImageTk.PhotoImage(spinning_image)
        spinning_label = tk.Label(loading_window, image=spinning_image)
        spinning_label.image = spinning_image
        spinning_label.pack()

        # Update the loading window and delay the main window
        loading_window.update()
        time.sleep(2)  # Adjust the timeout as needed (3 seconds in this case)

        # Close the loading window and display the main window
        loading_window.destroy()
        self.window.deiconify()

if __name__ == '__main__':
    app = ArcAngelGPT()
