from collections import deque
from dataclasses import dataclass, field
from datetime import datetime


def default_created_at() -> datetime.time:
    return datetime.time()


@dataclass
class FifoTask:
    priority: time.hour = field(default=0)
    created_at: time.hour = field(default_factory=default_created_at())

    name: str
    description: str
    status: int
    created_at: datetime.time()

    def __lt__(self, other: 'FifoTask') -> bool:
        if self.priority == other.priority:
            return self.created_at < other.created_at
        return self.priority > other.priority


task1 = deque['Music', 'Downloads', 2, ]
task2 = deque['Movie', 'Watching', 3]
task3 = deque['Program', 'Installing', 1]
