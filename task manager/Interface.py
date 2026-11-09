import tkinter as tk
from tkinter import messagebox

from AppLabel import AppLabel
from AppButton import AppButton
from AppListbox import AppListbox
from storage import Storage

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Neon Task Manager")
        self.root.geometry("500x520")
        self.root.minsize(450, 480)
        self.root.configure(bg="#1e1e24")

        self.storage = Storage()
        self.tasks = self.storage.load_tasks()


        self.title_label = AppLabel(
            self.root,
            text=" TASK MANAGER "
        )
        self.title_label.pack(pady=(25, 15))

        self.input_frame = tk.Frame(self.root, bg="#1e1e24")
        self.input_frame.pack(pady=10, padx=20, fill=tk.X)

        self.task_entry = tk.Entry(
            self.input_frame,
            font=("Segoe UI", 12),
            bg="#222831",
            fg="#eeeeee",
            insertbackground="#eeeeee",
            bd=0,
            highlightthickness=1,
            highlightbackground="#393e46"
        )
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=5)

        self.task_entry.bind(
            "<Return>",
            lambda event: self.add_task()
        )

        self.add_button = AppButton(
            self.input_frame,
            text="Добавить",
            command=self.add_task
        )
        self.add_button.pack(side=tk.RIGHT)


        self.task_list = AppListbox(self.root)
        self.task_list.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

        for task in self.tasks:
            self.task_list.add_task(task)


        self.delete_button = AppButton(
            self.root,
            text="Удалить выбранную задачу",
            command=self.delete_task,
            bg="#d9534f",
            activebackground="#c9302c"
        )
        self.delete_button.pack(pady=(0, 25), fill=tk.X, padx=20)

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_app
        )

    def add_task(self):
        task = self.task_entry.get().strip()

        if task:
            self.tasks.append(task)
            self.task_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.storage.save_tasks(self.tasks)
        else:
            messagebox.showwarning(
                "Внимание",
                "Нельзя добавить пустую задачу!"
            )

    def delete_task(self):
        selected = self.task_list.curselection()

        if selected:
            index = selected[0]
            self.task_list.delete_selected()
            self.tasks.pop(index)
            self.storage.save_tasks(self.tasks)
        else:
            messagebox.showwarning(
                "Внимание",
                "Сначала выберите задачу из списка!"
            )

    def close_app(self):
        self.storage.save_tasks(self.tasks)
        self.root.destroy()

    def run(self):
        self.root.mainloop()
