import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent,
            text=text,
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            **kwargs
        )
