import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            font=("Arial", 12),
            width=45,
            height=10,
            selectmode=tk.SINGLE,
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
