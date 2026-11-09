import tkinter as tk

class AppListbox(tk.Listbox):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            font=("Segoe UI", 11),
            width=42,
            height=11,
            selectmode=tk.SINGLE,
            bg="#222831",       
            fg="#eeeeee",      
            selectbackground="#00adb5",
            selectforeground="#1e1e24",
            highlightthickness=1,
            highlightbackground="#393e46",
            bd=0,
            **kwargs
        )

    def add_task(self, task):
        self.insert(tk.END, task)

    def delete_selected(self):
        selected = self.curselection()
        if selected:
            self.delete(selected[0])

    def get_tasks(self):
        return list(self.get(0, tk.END))
