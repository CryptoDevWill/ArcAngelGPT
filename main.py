import tkinter as tk
from view.gui.gui import GUI
from view.gui.menu import Menu
from view.screens.loading import show_loading_screen


class ArcAngelGPT:
    def __init__(self):
        self.window = tk.Tk()
        show_loading_screen(self.window)
        GUI(self.window)
        Menu(self.window)
        self.window.mainloop()

if __name__ == '__main__':
    app = ArcAngelGPT()
