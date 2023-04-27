import tkinter as tk
from data.global_variables import current_tasks_array

def create_steps_box(parent):
    steps_box = tk.LabelFrame(parent, text="Steps", bg='#2d2d2d', fg='#ffffff')
    for index, step in enumerate(current_tasks_array.get()):
        step_text = list(step.values())[0]
        step_complete = list(step.values())[1]

        if step_complete:
            status_symbol = "✓"
            status_color = "#00ff00"  # Green
        else:
            status_symbol = "●"
            status_color = "#ff9900"  # Orange

        step_label = tk.Label(steps_box, text=f"{step_text}", bg='#2d2d2d', fg='#ffffff')
        step_label.grid(row=index, column=1, sticky="w", padx=(0, 10), pady=5)

        status_label = tk.Label(steps_box, text=status_symbol, bg='#2d2d2d', fg=status_color)
        status_label.grid(row=index, column=0, sticky="w", padx=10, pady=5)

    return steps_box
