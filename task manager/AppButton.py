import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Arial", 11),
            cursor="hand2",
            **kwargs
        )
