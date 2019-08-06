import typing
from dataclasses import dataclass, field

from src.to_do.deque import fifo_task


class Fifo:
    tasks: typing.List[fifo_task] = field(default_factory=list)

    def add_task(self, task) -> None:
        self.tasks.append(task)

    def get_task(self) -> fifo_task:
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop(0)


