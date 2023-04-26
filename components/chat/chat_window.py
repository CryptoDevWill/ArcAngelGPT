import tkinter as tk
from data.conversation import conversation
from data.global_variables import work_mode


class ChatWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.mode_label = tk.Label(self,
                                   text="Work Mode" if work_mode.get() else "Chill Mode",
                                   font=("Arial", 12),
                                   bg='green' if work_mode.get() else 'blue',
                                   fg='white')
        self.mode_label.pack(side=tk.TOP, anchor=tk.W)


        self.conversation_listbox = tk.Listbox(self, bg='#1e1e1e', fg='white', width=80, height=20, selectbackground='#1e1e1e', selectforeground='white')
        self.conversation_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self, command=self.conversation_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.conversation_listbox.config(yscrollcommand=self.scrollbar.set)

    def update_conversation(self):
        global conversation
        self.conversation_listbox.delete(0, tk.END)
        print(work_mode.get())
        if work_mode.get():
            self.mode_label.configure(text="Work Mode", bg='#3a9d23')  # Changed to a dark green color
            self.conversation_listbox.configure(bg='#1e1e1e')
        else:
            self.mode_label.configure(text="Chill Mode", bg='blue')
            self.conversation_listbox.configure(bg='#1e1e1e')

        for msg in conversation[1:]:
            role = msg['role']
            content = msg['content']
            formatted_msg = f"{role.capitalize()}: {content}"
            self.conversation_listbox.insert(tk.END, formatted_msg)

            if role == 'user':
                self.conversation_listbox.itemconfigure(tk.END, bg='#405068', fg='white')
            elif role == 'assistant':
                self.conversation_listbox.itemconfigure(tk.END, bg='#2f3d4a', fg='white')
            elif role == 'system':
                self.conversation_listbox.itemconfigure(tk.END, bg='#2d2d2d', fg='#ff9d00')
    
