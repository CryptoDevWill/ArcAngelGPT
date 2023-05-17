import tkinter as tk
from controller.data.global_variables import WorkMode
from controller.play_sound import play_sound


class WorkModeLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.update_label()
        WorkMode().set_callback(self.update_label)
        self.pack(fill="x", expand=True)
        
    def update_label(self):
        if WorkMode().get():
            self.config(text="Work Mode", bg="#007f00", fg="white")
            play_sound('work')
        else:
            self.config(text="Chill Mode", bg="#00007f", fg="white")
