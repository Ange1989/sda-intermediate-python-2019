from unittest import TestCase

from src.to_do.deque import Fifo
from src.to_do.deque.fifo_task import FifoTask


class TestFifo(TestCase):
    def test_should_add_one_task(self):
        fifo = Fifo()

        fifo.add_task(task1)
        fifo.add_task(task2)
        fifo.add_task(task3)


if __name__ == '__main__':
    task1 = FifoTask['Music', 'Downloads', 2]
    task2 = FifoTask['Movie', 'Watching', 3]
    task3 = FifoTask['Program', 'Installing', 1]