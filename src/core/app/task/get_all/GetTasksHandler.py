from typing import List

from src.core.app.task.get_all.GetTasks import GetTasks
from src.core.domain.Task import Task
from src.core.domain.Tasks import Tasks
from src.core.infrastructure.bus.Handler import Handler


class GetTasksHandler(Handler):
    def __init__(self, tasks: Tasks):
        self.__tasks = tasks

    def execute(self, request: GetTasks) -> List[Task]:
        return self.__tasks.get_all()
