from src.base.Id import Id
from src.core.app.task.delete.DeleteTask import DeleteTask
from src.core.domain.Tasks import Tasks
from src.core.infrastructure.bus.Handler import Handler


class DeleteTaskHandler(Handler):
    name = 'DeleteTask'

    def __init__(self, tasks: Tasks):
        self.__tasks = tasks

    def execute(self, request: DeleteTask) -> Id:
        self.__tasks.delete_task(request.task_id)
        return request.task_id
