from datetime import datetime

from src.base.Id import Id


class TaskSnapshot:
    def __init__(self, id: Id, title: str, description: str, date: datetime) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.date = date


class Task:
    def __init__(self, id: Id, title: str, description: str, date: datetime) -> None:
        self.__id = id
        self.__title = title
        self.__description = description
        self.__date = date

    @property
    def id(self) -> Id:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def date(self) -> datetime:
        return self.__date

    @staticmethod
    def from_snapshot(snapshot: TaskSnapshot):
        return Task(snapshot.id, snapshot.title, snapshot.description, snapshot.date)
