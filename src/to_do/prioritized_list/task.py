from dataclasses import dataclass, field

from datetime import datetime, timedelta


def default_deadline() -> datetime:
    return datetime.now() + timedelta(days=2)


@dataclass
class PrioritizedTask:
    name: str
    description: str
    priority: int = field(default=0)
    deadline: datetime = field(default_factory=default_deadline)

    def __repr__(self):
        return f'{self.name}: {self.description}'

    def __lt__(self, other: 'PrioritizedTask') -> bool:
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority > other.priority


task_01 = PrioritizedTask('cleaning', 'cleaning bathroom', 0, datetime(2019, 5, 1))
task_02 = PrioritizedTask('dishes', 'cleaning the dishes', 4, datetime(2019, 6, 1))
task_03 = PrioritizedTask('shopping', 'buy some food', 3, datetime(2019, 4, 1))
task_04 = PrioritizedTask('homework', 'do the homework', 2)
task_05 = PrioritizedTask('call', 'call my friend', 0)
