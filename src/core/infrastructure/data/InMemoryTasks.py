from src.base.Id import Id
from src.core.domain import Task
from src.core.domain.Tasks import Tasks


class InMemoryTasks(Tasks):
    def __init__(self) -> None:
        self.__tasks = []
        self.__next_id = Id(0)

    def next_id(self) -> Id:
        self.__next_id = Id(self.__next_id.value + 1)
        return self.__next_id

    def add_task(self, task: Task) -> None:
        self.__tasks.append(task)

    def delete_task(self, task_id: Id) -> None:
        for task in self.__tasks:
            if task.id == task_id:
                self.__tasks.remove(task)
                break

    def update_task(self, task: Task) -> None:
        pass

    def get_task(self, task_id: Id) -> Task:
        for task in self.__tasks:
            if task.id == task_id:
                return task
        return None

    def find_by(self, title: str, description: str) -> Task:
        for task in self.__tasks:
            if task.title == title and task.description == description:
                return task
        return None

    def get_all(self) -> list[Task]:
        return self.__tasks
