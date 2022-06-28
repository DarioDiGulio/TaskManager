from datetime import datetime

from src.base.Id import Id
from src.core.app.new_task.NewTask import NewTask
from src.core.domain.Task import Task
from src.core.domain.Tasks import Tasks
from src.core.infrastructure.bus.Handler import Handler


class NewTaskHandler(Handler):
    def __init__(self, tasks: Tasks):
        self.__tasks = tasks

    def execute(self, request: NewTask) -> Id:
        self.__fail_with_invalid_task(request)
        next_id = self.__tasks.next_id()
        date = datetime.strptime(request.due_date, '%d/%m/%Y')
        new_task = Task(next_id, request.title, request.description, date)
        self.__tasks.add_task(new_task)
        return next_id

    def __fail_with_invalid_task(self, request):
        if request.title is None or request.title == '':
            raise AttributeError('Title is required')
