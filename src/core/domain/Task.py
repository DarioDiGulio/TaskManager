from datetime import datetime

from src.base.Id import Id


class Task:
    def __init__(self, id: Id, title: str, description: str, date: datetime) -> None:
        self.__id = id
        self.__title = title

    @property
    def id(self) -> Id:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title
