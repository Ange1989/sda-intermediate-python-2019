from dataclasses import dataclass, field
from datetime import datetime

from src.to_do.base_list import BaseTask


def default_created_at() -> datetime:
    return datetime.now()


@dataclass
class FifoTask(BaseTask):
    status: int
    # created_at: datetime = field(default_factory=datetime.now)
    created_at: datetime = field(default_factory=default_created_at)


task1 = FifoTask('Music', 'Downloads', 2, )
task2 = FifoTask('Movie', 'Watching', 3, )
task3 = FifoTask('Program', 'Installing', 1, )
