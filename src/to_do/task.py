from dataclasses import dataclass


# @dataclass(frozen=True)
@dataclass
class BacklogTask:
    name: str
    description: str

    def __repr__(self):
        print(f'{self.name}: {self.description}')


task_01 = BacklogTask('cleaning', 'cleaning bathroom')
task_02 = BacklogTask('dishes', 'cleaning the dishes')
task_03 = BacklogTask('shopping', 'buy some food')
task_04 = BacklogTask('homework', 'do the homework')
task_05 = BacklogTask('call', 'call my friend')
