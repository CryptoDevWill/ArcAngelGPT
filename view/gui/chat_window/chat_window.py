import tkinter as tk
from controller.data.conversation import Conversation

class ChatWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.conversation_text = tk.Text(self, bg='#1e1e1e', fg='white', selectforeground='yellow', selectbackground='red', highlightthickness=0, width=80, height=20, font=('Arial', 14), wrap=tk.WORD, exportselection=True)
        self.conversation_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.conversation_text.config(state=tk.DISABLED)

        self.conversation_text.bind("<Control-c>", self.copy_text)
        self.conversation_text.bind("<Control-v>", self.paste_text)
        self.conversation_text.bind("<B1-Motion>", self.highlight_selected_text)

        self.prev_bg_color = self.conversation_text.cget('bg')
        self.prev_fg_color = self.conversation_text.cget('fg')

    def copy_text(self, event):
        try:
            selected_text = self.conversation_text.selection_get()
            self.clipboard_clear()
            self.clipboard_append(selected_text)
        except:
            pass

    def highlight_selected_text(self, event):
        sel = self.conversation_text.tag_ranges("sel")
        if not sel:
            self.conversation_text.configure(bg=self.prev_bg_color, fg=self.prev_fg_color)
            return

        self.conversation_text.tag_remove("highlight", "1.0", tk.END)
        start = self.conversation_text.index("sel.first")
        end = self.conversation_text.index("sel.last")
        self.conversation_text.tag_add("highlight", start, end)
        self.conversation_text.tag_configure("highlight", background="#ffffff")

    def paste_text(self, event):
        pass

    def update_conversation(self):
        self.conversation_text.config(state=tk.NORMAL)
        self.conversation_text.delete(1.0, tk.END)
        self.conversation_text.configure(bg='#1e1e1e')

        for msg in Conversation.instance()[1:]:
            role = msg['role']
            if role == 'system':
                continue
            content = msg['content']
            formatted_msg = f"{role.capitalize()}: {content}\n"
            self.conversation_text.insert(tk.END, formatted_msg, role)
            self.conversation_text.tag_configure("user", background="#1f1f1f", foreground="white")
            self.conversation_text.tag_configure("assistant", background="#2f3d4a", foreground="white")

        self.conversation_text.see(tk.END)
        self.conversation_text.config(state=tk.DISABLED)

