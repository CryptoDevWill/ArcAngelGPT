import tkinter as tk
from controller.data.global_variables import Thinking

class ThinkingIndicator(tk.Label):
    def __init__(self, master=None, bg=None, fg=None, **kwargs):
        super().__init__(master, bg=bg, fg=fg, **kwargs)
        self.thinking = False
        self.dots_count = 0
        self.after_id = None
        self.check_thinking()

    def set_thinking(self, thinking):
        self.thinking = thinking
        if thinking:
            self.update_dots()
        else:
            if self.after_id is not None:
                self.after_cancel(self.after_id)
            self.config(text=" ")

    def update_dots(self):
        if self.thinking:
            self.dots_count = (self.dots_count + 1) % 8
            dots = "." * self.dots_count
            self.config(text=f"{dots}")
            self.after_id = self.after(500, self.update_dots)

    def check_thinking(self):
        thinking = Thinking()
        current_thinking = thinking.get()
        if current_thinking != self.thinking:
            self.set_thinking(current_thinking)
        self.after(500, self.check_thinking)
