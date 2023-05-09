import tkinter as tk

class UserInput:
    def __init__(self, master, on_return_press, max_input_length=100):
        self.master = master
        self.max_input_length = max_input_length
        self.char_count = 0

        self.user_input = tk.Entry(
            self.master,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#cccccc',
            font=('Helvetica', 16),
            fg='white',
            bg='#2d2d2d',
            relief='flat',
            insertbackground='white',
            validate='key',
            validatecommand=(self.master.register(self.validate_input), '%P')
        )
        self.user_input.pack(side='left', fill='x', expand=True)

        self.user_input.bind('<Return>', on_return_press)

        # Add character counter
        self.char_counter = tk.Label(
            self.master,
            text=f'0/{self.max_input_length}',
            font=('Helvetica', 12),
            fg='#999999',
            bg='#2d2d2d'
        )
        self.char_counter.pack(side='right', padx=(0, 10))

        # Bind key events to update character counter
        self.user_input.bind('<KeyRelease>', self.update_char_counter)

    def get_text(self):
        return self.user_input.get()

    def clear_text(self):
        self.user_input.delete(0, 'end')

    def update_char_counter(self, event):
        input_text = self.user_input.get()
        self.char_count = len(input_text)
        self.char_counter.config(text=f'{self.char_count}/{self.max_input_length}')
        if self.char_count == self.max_input_length:
            self.char_counter.config(fg='#a10000')
        else:
            self.char_counter.config(fg='#999999')

    def validate_input(self, input_text):
        return len(input_text) <= self.max_input_length
