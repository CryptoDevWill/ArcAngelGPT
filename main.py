import tkinter as tk
from gui.gui import GUI
from gui.menu import Menu

class ArcAngelGPT:
    def __init__(self):
        self.window = tk.Tk()
        GUI(self.window)
        Menu(self.window)
        self.window.mainloop()
if __name__ == '__main__':
    app = ArcAngelGPT()
