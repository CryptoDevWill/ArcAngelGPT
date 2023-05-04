import tkinter as tk

class UrlInput:
    def __init__(self, master):
        self.master = master

        # Create a new frame to contain the URL label and the input field
        self.url_frame = tk.Frame(self.master, bg='#2d2d2d')
        self.url_frame.pack(side='top', fill='x', expand=True, pady=(0, 5))

        # Move the URL label inside the new frame
        self.url_label = tk.Label(
            self.url_frame,
            text='URL:',
            font=('Helvetica', 14),
            fg='white',
            bg='#2d2d2d'
        )
        self.url_label.pack(side='left')  # Pack the label with side='left' inside the new frame

        self.url_input = tk.Entry(
            self.url_frame,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#cccccc',
            font=('Helvetica', 14),
            fg='white',
            bg='#000000',
            relief='flat',
            insertbackground='white'
        )
        self.url_input.pack(side='left', fill='x', expand=True)  # Pack the input field with side='left' inside the new frame

    def get_url(self):
        return self.url_input.get()

    def clear_url(self):
        self.url_input.delete(0, 'end')
