import tkinter as tk

class AppLabel(tk.Label):
    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent,
            text=text,
            font=("Segoe UI", 22, "bold"),
            bg="#1e1e24",        
            fg="#00adb5",       
            **kwargs
        )
