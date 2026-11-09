
import tkinter as tk
from tkinter import messagebox

from AppLabel import AppLabel
from AppButton import AppButton
from AppListbox import AppListbox
from storage import Storage


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.root.geometry("600x450")
        self.root.minsize(400, 350)
        self.root.configure(bg="#f0f0f0")

        self.storage = Storage()
        self.tasks = self.storage.load_tasks()

        self.title_label = AppLabel(
            self.root,
            text="Task Manager"
        )
        self.title_label.pack(pady=20)

        self.task_entry = tk.Entry(
            self.root,
            font=("Arial", 12),
            width=35
        )
        self.task_entry.pack(pady=10)

        self.task_entry.bind(
            "<Return>",
            lambda event: self.add_task()
        )

        self.add_button = AppButton(
            self.root,
            text="Добавить задачу",
            command=self.add_task
        )
        self.add_button.pack(pady=5)

        self.task_list = AppListbox(self.root)
        self.task_list.pack(pady=10)

        for task in self.tasks:
            self.task_list.add_task(task)

        self.delete_button = AppButton(
            self.root,
            text="Удалить задачу",
            command=self.delete_task
        )
        self.delete_button.pack(pady=5)

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
                "Предупреждение",
                "Введите название задачи!"
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
                "Предупреждение",
                "Выберите задачу для удаления!"
            )

    def close_app(self):
        self.storage.save_tasks(self.tasks)
        self.root.destroy()

    def run(self):
        self.root.mainloop()
