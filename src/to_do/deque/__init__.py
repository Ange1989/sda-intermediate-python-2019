import abc
from dataclasses import dataclass

from src.to_do.deque import fifo_task


@dataclass
class Fifo:

    @abc.abstractmethod
    def add_task(self, task) -> None:
        self.tasks.append(task)

    @abc.abstractmethod
    def get_task(self) -> fifo_task:
        if len(self.task) == 0:
            return None
        return self.task.popleft()
