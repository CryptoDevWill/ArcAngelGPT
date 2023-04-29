import tkinter as tk
from data.conversation import conversation
from data.global_variables import work_mode


class ChatWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.mode_label = tk.Label(self,
            text="Work Mode" if work_mode.get() else "Chill Mode",
            font=("Arial", 14),
            bg='#008e02' if work_mode.get() else '#0005c5',
            fg='white')
        self.mode_label.pack(side=tk.TOP, anchor=tk.W)

        self.conversation_text = tk.Text(self, bg='#1e1e1e', fg='white', highlightthickness=0, width=80, height=20, font=('Arial', 14), wrap=tk.WORD)
        self.conversation_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.conversation_text.config(state=tk.DISABLED)  # Disable editing of the Text widget

    def update_conversation(self):
        global conversation
        self.conversation_text.config(state=tk.NORMAL)  # Enable editing to update the conversation
        self.conversation_text.delete(1.0, tk.END)
        if work_mode.get():
            self.mode_label.configure(text="Work Mode", bg='#3a9d23')  # Changed to a dark green color
            self.conversation_text.configure(bg='#1e1e1e')
        else:
            self.mode_label.configure(text="Chill Mode", bg='blue')
            self.conversation_text.configure(bg='#1e1e1e')

        for msg in conversation[1:]:
            role = msg['role']
            content = msg['content']
            formatted_msg = f"{role.capitalize()}: {content}\n"
            self.conversation_text.insert(tk.END, formatted_msg, role)
            self.conversation_text.tag_configure("user", background="#405068", foreground="white")
            self.conversation_text.tag_configure("assistant", background="#2f3d4a", foreground="white")
            self.conversation_text.tag_configure("system", background="#2d2d2d", foreground="#ff9d00")

        self.conversation_text.see(tk.END)  # Automatically scroll to the end of the conversation
        self.conversation_text.config(state=tk.DISABLED)  # Disable editing after updating the conversation

