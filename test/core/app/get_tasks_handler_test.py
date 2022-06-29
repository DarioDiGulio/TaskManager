from unittest import TestCase

from src.core.app.get_tasks.GetTasks import GetTasks
from src.core.app.get_tasks.GetTasksHandler import GetTasksHandler
from src.core.infrastructure.data.InMemoryTasks import InMemoryTasks
from test.core.domain.TaskBuilder import task


class GetTasksTest(TestCase):

    def test_get_tasks(self):
        self.tasks.add_task(task())
        self.tasks.add_task(task())
        self.tasks.add_task(task())

        tasks = self.handler.execute(GetTasks())

        self.assertEqual(3, len(tasks))

    def setUp(self) -> None:
        self.tasks = InMemoryTasks()
        self.handler = GetTasksHandler(self.tasks)
