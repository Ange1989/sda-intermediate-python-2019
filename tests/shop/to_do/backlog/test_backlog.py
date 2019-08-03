from unittest import TestCase

from src.to_do.backlog import Backlog
# from src.to_do.backlog.backlog import Backlog
from src.to_do.backlog.task import task_03, task_01, task_02


class TestBacklog(TestCase):
    def test_should_add_one_task(self):
        # GIVEN
        backlog = Backlog()

        # WHEN
        backlog.add_task(task_03)

        # THEN
        self.assertListEqual([task_03], backlog.tasks)

    def test_should_add_three_tasks(self):
        # GIVEN
        backlog = Backlog()

        # WHEN
        backlog.add_task(task_03)
        backlog.add_task(task_01)
        backlog.add_task(task_02)

        # THEN
        self.assertListEqual([task_03, task_01, task_02], backlog.tasks)

    def test_should_get_task(self):
        # GIVEN
        backlog = Backlog()
        backlog.add_task(task_03)
        backlog.add_task(task_01)
        backlog.add_task(task_02)

        # WHEN
        actual_task = backlog.get_task()

        # THEN
        self.assertEqual(task_02, actual_task)

    def test_get_task_from_empty_list(self):
        # GIVEN
        backlog = Backlog()

        # WHEN
        actual_task = backlog.get_task()

        # THEN
        self.assertEqual(None, actual_task)
