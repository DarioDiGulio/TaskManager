import unittest
from unittest import TestCase

from src.core.app.new_task.NewTask import NewTask
from src.core.app.new_task.NewTaskHandler import NewTaskHandler
from src.core.infrastructure.data.InMemoryTasks import InMemoryTasks


class NewTaskTest(TestCase):

    def test_add_task(self):
        new_task = NewTask('New Task', 'Some description', '12/12/2020')

        new_task_id = self.handler.execute(new_task)

        saved_task = self.tasks.get_task(new_task_id)
        self.assertEqual(saved_task.title, 'New Task')

    def setUp(self) -> None:
        self.tasks = InMemoryTasks()
        self.handler = NewTaskHandler(self.tasks)


if __name__ == '__main__':
    unittest.main()
