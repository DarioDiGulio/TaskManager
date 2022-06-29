from src.core.app.task.delete.DeleteTasksHandler import DeleteTaskHandler
from src.core.app.task.get_all.GetTasksHandler import GetTasksHandler
from src.core.app.task.new.NewTaskHandler import NewTaskHandler
from src.core.infrastructure.bus.CoreExecutor import CoreExecutor
from src.core.infrastructure.data.InMemoryTasks import InMemoryTasks


class Core:
    def __init__(self):
        self.__executor = CoreExecutor()
        self.__tasks = InMemoryTasks()
        self.register_handlers()

    def register_handlers(self) -> None:
        self.__executor.register_handler(GetTasksHandler(self.__tasks))
        self.__executor.register_handler(NewTaskHandler(self.__tasks))
        self.__executor.register_handler(DeleteTaskHandler(self.__tasks))

    def execute(self, request) -> None:
        self.__executor.execute(request)


core = Core()
