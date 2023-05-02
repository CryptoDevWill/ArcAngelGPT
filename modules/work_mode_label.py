import tkinter as tk
from data.global_variables import work_mode
from functions.play_sound import play_sound

class WorkModeLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.update_label()
        work_mode.set_callback(self.update_label)
        self.pack(fill="x", expand=True)
        
    def update_label(self):
        if work_mode.get():
            self.config(text="Work Mode", bg="#007f00", fg="white")
            play_sound('work')
        else:
            self.config(text="Chill Mode", bg="#00007f", fg="white")
