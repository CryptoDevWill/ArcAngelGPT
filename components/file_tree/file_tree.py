import tkinter as tk
from functions.get_file_tree import get_file_tree
import os
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileTree(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.tree_text = tk.Text(self, state=tk.DISABLED, width=70, bg='black', fg='white', highlightthickness=0, padx=10, pady=10)
        self.tree_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define tags for colors
        self.tree_text.tag_configure("folder", foreground="#A9A9A9")
        self.tree_text.tag_configure("python_file", foreground="#1aa8e5")
        self.tree_text.tag_configure("js_file", foreground="#cbad00")
        self.tree_text.tag_configure("file", foreground="#babeba")

        # Bind callback functions
        self.tree_text.tag_bind("folder", "<Button-1>", self.open_folder)
        self.tree_text.tag_bind("python_file", "<Button-1>", self.open_file)
        self.tree_text.tag_bind("js_file", "<Button-1>", self.open_file)
        self.tree_text.tag_bind("file", "<Button-1>", self.open_file)

        # Bind cursor change on hover
        self.tree_text.tag_bind("folder", "<Enter>", lambda e: self.tree_text.config(cursor="hand2"))
        self.tree_text.tag_bind("python_file", "<Enter>", lambda e: self.tree_text.config(cursor="hand2"))
        self.tree_text.tag_bind("js_file", "<Enter>", lambda e: self.tree_text.config(cursor="hand2"))
        self.tree_text.tag_bind("file", "<Enter>", lambda e: self.tree_text.config(cursor="hand2"))

        self.tree_text.tag_bind("folder", "<Leave>", lambda e: self.tree_text.config(cursor=""))
        self.tree_text.tag_bind("python_file", "<Leave>", lambda e: self.tree_text.config(cursor=""))
        self.tree_text.tag_bind("js_file", "<Leave>", lambda e: self.tree_text.config(cursor=""))
        self.tree_text.tag_bind("file", "<Leave>", lambda e: self.tree_text.config(cursor=""))

        self.update_tree()
        self.start_file_system_observer()

    def update_tree(self):
        tree_lines, tree_tags = get_file_tree()

        self.tree_text.config(state=tk.NORMAL)
        self.tree_text.delete('1.0', tk.END)

        for line, (tag, path) in zip(tree_lines, tree_tags):
            self.tree_text.insert(tk.END, line + '\n', (tag, path))

        self.tree_text.config(state=tk.DISABLED)

    def open_folder(self, event):
        tags = self.tree_text.tag_names(tk.CURRENT)
        folder_path = tags[1]
        if os.name == 'nt':  # Windows
            os.startfile(folder_path)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['open', folder_path])

    def open_file(self, event):
        tags = self.tree_text.tag_names(tk.CURRENT)
        file_path = tags[1]
        folder_path = str(Path(file_path).parent)  # Get the folder containing the file
        if os.name == 'nt':  # Windows
            os.startfile(folder_path)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['open', folder_path])

    def start_file_system_observer(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = self.on_file_system_modified
        self.observer = Observer()
        self.observer.schedule(event_handler, ".", recursive=True)
        self.observer.start()

    def on_file_system_modified(self, event):
        self.update_tree()

    def close(self):
        self.observer.stop()
        self.observer.join()
