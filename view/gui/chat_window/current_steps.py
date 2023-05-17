import tkinter as tk

from base import Instance


class TaskObserver:
    def update(self):
        pass


class CurrentTasksArray(metaclass=Instance):
    def __init__(self):
        self.value = []
        self.observers = []

    def set(self, state):
        self.value = state
        self._notify_observers()

    def get(self):
        return self.value

    def _notify_observers(self):
        for observer in self.observers:
            observer.update()

    def add_observer(self, observer):
        if not isinstance(observer, TaskObserver):
            raise TypeError("Observer must be an instance of TaskObserver")
        self.observers.append(observer)


class StepsBox(tk.LabelFrame, TaskObserver):
    def __init__(self, parent):
        tk.LabelFrame.__init__(self, parent, text="Steps", bg='#2d2d2d', fg='#ffffff')
        TaskObserver.__init__(self)
        self.parent = parent
        self.update()
        CurrentTasksArray().add_observer(self)

    def update(self):
        for widget in self.winfo_children():
            widget.destroy()

        for index, step in enumerate(CurrentTasksArray().get()):
            step_text = step["step"]
            step_complete = step["complete"]

            if step_complete:
                status_symbol = "✓"
                status_color = "#00ff00"  # Green
            else:
                status_symbol = "●"
                status_color = "#ff9900"  # Orange

            step_label = tk.Label(self, text=f"{step_text}", bg='#2d2d2d', fg='#ffffff')
            step_label.grid(row=index, column=1, sticky="w", padx=(0, 10), pady=5)

            status_label = tk.Label(self, text=status_symbol, bg='#2d2d2d', fg=status_color)
            status_label.grid(row=index, column=0, sticky="w", padx=10, pady=5)


def create_steps_box(parent):
    return StepsBox(parent)
