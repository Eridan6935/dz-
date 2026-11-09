import json
import os


class Storage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                tasks = json.load(file)

                if isinstance(tasks, list):
                    return tasks

                return []

        except (json.JSONDecodeError, OSError):
            return []

    def save_tasks(self, tasks):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                tasks,
                file,
                ensure_ascii=False,
                indent=4
            )
