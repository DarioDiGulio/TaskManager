from datetime import datetime

from src.base.Id import Id
from src.core.domain.Task import Task, TaskSnapshot

next_id = 0


class TaskBuilder:
    def __init__(self):
        self.__title = 'Some title'
        self.__description = 'Some description'
        self.__id = Id(next_id + 1)
        self.__due_date = datetime(2020, 1, 1)

    def id(self, id: Id):
        self.__id = id
        return self

    def id(self, id: int):
        self.__id = Id(id)
        return self

    def title(self, title: str):
        self.__title = title
        return self

    def description(self, description: str):
        self.__description = description
        return self

    def due_date(self, due_date: datetime):
        self.__due_date = due_date
        return self

    def due_date(self, due_date: str):
        date = datetime.strptime(due_date, '%d/%m/%Y')
        self.__due_date = date
        return self

    def build(self):
        return Task.from_snapshot(TaskSnapshot(self.__id, self.__title, self.__description, self.__due_date))


def task(changes=None):
    task_builder = TaskBuilder()
    if changes:
        changes(task_builder)
    return task_builder.build()
