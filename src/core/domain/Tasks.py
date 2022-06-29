from abc import abstractmethod

from src.base.Id import Id
from src.core.domain import Task


class Tasks:
    @abstractmethod
    def next_id(self) -> Id:
        pass

    @abstractmethod
    def add_task(self, task: Task) -> None:
        pass

    @abstractmethod
    def delete_task(self, task_id: Id) -> None:
        pass

    @abstractmethod
    def update_task(self, task: Task) -> None:
        pass

    @abstractmethod
    def get_task(self, task_id: Id) -> Task:
        pass

    @abstractmethod
    def find_by(self, title: str, description: str) -> Task:
        pass

    @abstractmethod
    def get_all(self) -> list[Task]:
        pass
