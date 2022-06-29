from unittest import TestCase

from test.core.domain.TaskBuilder import task
from src.base.Id import Id
from src.core.app.task.delete.DeleteTask import DeleteTask
from src.core.app.task.delete.DeleteTasksHandler import DeleteTaskHandler
from src.core.infrastructure.data.InMemoryTasks import InMemoryTasks


class DeleteTaskHandlerTest(TestCase):
    def test_delete_task_handler(self):
        self.tasks.add_task(task(lambda builder: builder.id(1)))

        self.handler.execute(DeleteTask(Id(1)))

        self.assertIsNone(self.tasks.get_task(Id(1)))

    def test_delete_task_returns_id_deleted(self):
        self.tasks.add_task(task(lambda builder: builder.id(1)))

        self.assertEqual(Id(1), self.handler.execute(DeleteTask(Id(1))))

    def setUp(self) -> None:
        self.tasks = InMemoryTasks()
        self.handler = DeleteTaskHandler(self.tasks)
