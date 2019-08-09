from unittest import TestCase

from src.to_do.deque import Fifo
from src.to_do.deque.fifo_task import task1, task2, task3


class TestFifo(TestCase):
    def test_should_add_one_task(self):
        fifo = Fifo()

        fifo.add_task(task1)
        fifo.add_task(task2)
        fifo.add_task(task3)
