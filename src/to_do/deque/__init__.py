import typing
from collections import deque
from dataclasses import dataclass, field

from src.to_do.base_list import BaseListTask
from src.to_do.deque.fifo_task import FifoTask


@dataclass
class Fifo(BaseListTask):
    tasks: typing.Deque[FifoTask] = field(default_factory=deque)

    def add_task(self, task: FifoTask) -> None:
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[FifoTask]:
        if len(self.tasks) == 0:
            return None
        return self.tasks.popleft()
