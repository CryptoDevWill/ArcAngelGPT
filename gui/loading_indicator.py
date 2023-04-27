import tkinter as tk
from data.global_variables import loading

class LoadingIndicator(tk.Label):
    def __init__(self, master=None, bg=None, fg=None, **kwargs):
        super().__init__(master, bg=bg, fg=fg, **kwargs)
        self.loading = False
        self.dots_count = 0
        self.after_id = None
        self.check_loading()

    def set_loading(self, loading):
        self.loading = loading
        if loading:
            self.update_dots()
        else:
            if self.after_id is not None:
                self.after_cancel(self.after_id)
            self.config(text=" ")

    def update_dots(self):
        if self.loading:
            self.dots_count = (self.dots_count + 1) % 8
            dots = "." * self.dots_count
            self.config(text=f"{dots}")
            self.after_id = self.after(500, self.update_dots)

    def check_loading(self):
        global loading
        current_loading = loading.get()
        if current_loading != self.loading:
            self.set_loading(current_loading)
        self.after(500, self.check_loading)
