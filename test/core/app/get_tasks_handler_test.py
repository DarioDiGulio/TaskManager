from unittest import TestCase

from src.core.app.task.get_all.GetTasks import GetTasks
from src.core.app.task.get_all.GetTasksHandler import GetTasksHandler
from src.core.infrastructure.data.InMemoryTasks import InMemoryTasks
from test.core.domain.TaskBuilder import task


class GetTasksHandlerTest(TestCase):

    def test_get_tasks(self):
        self.tasks.add_task(task())
        self.tasks.add_task(task())
        self.tasks.add_task(task())

        tasks = self.handler.execute(GetTasks())

        self.assertEqual(3, len(tasks))

    def setUp(self) -> None:
        self.tasks = InMemoryTasks()
        self.handler = GetTasksHandler(self.tasks)
