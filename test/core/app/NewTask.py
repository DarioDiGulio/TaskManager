from datetime import datetime
from unittest import TestCase

from src.core.app.new_task.NewTask import NewTask
from src.core.app.new_task.NewTaskHandler import NewTaskHandler
from src.core.domain.TaskAlreadyExistsException import TaskAlreadyExistsException
from src.core.infrastructure.data.InMemoryTasks import InMemoryTasks
from test.core.domain.TaskBuilder import task


class NewTaskTest(TestCase):

    def test_add_task(self):
        command = NewTask('New Task', 'Some description', '12/12/2020')

        new_task_id = self.handler.execute(command)

        saved_task = self.tasks.get_task(new_task_id)
        self.assertEqual(saved_task.title, 'New Task')
        self.assertEqual(saved_task.description, 'Some description')
        self.assertEqual(saved_task.date, datetime(2020, 12, 12))

    def test_fail_if_title_is_empty(self):
        new_task = NewTask('', 'Some description', '12/12/2020')

        with self.assertRaises(AttributeError):
            self.handler.execute(new_task)

    def test_fail_if_task_already_exists(self):
        self.tasks.add_task(task(
            lambda builder: builder
            .title('New Task')
            .description('Some description')
        ))

        new_task = NewTask('New Task', 'Some description', '12/12/2020')
        with self.assertRaises(TaskAlreadyExistsException):
            self.handler.execute(new_task)

    def setUp(self) -> None:
        self.tasks = InMemoryTasks()
        self.handler = NewTaskHandler(self.tasks)
