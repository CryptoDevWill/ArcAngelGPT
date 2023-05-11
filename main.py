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

        running = True

        def toggle_running():
            nonlocal running
            running = False

        self.window.protocol("WM_DELETE_WINDOW", lambda: toggle_running())
        while running:
            self.window.update()


if __name__ == '__main__':
    app = ArcAngelGPT()
