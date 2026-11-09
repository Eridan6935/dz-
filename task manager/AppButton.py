import tkinter as tk

class AppButton(tk.Button):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            bg="#393e46",        
            fg="#eeeeee",        
            activebackground="#00adb5", 
            activeforeground="#1e1e24",
            bd=0,               
            padx=15,
            pady=8,
            **kwargs
        )
