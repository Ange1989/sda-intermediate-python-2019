import typing
from collections import namedtuple

sum_ints = lambda a, b: a + b

Employee = namedtuple('Employee', ['name', 'role', 'salary'])

if __name__ == '__main__':
    print(sum_ints(2, 3))
    list1 = [2, 5, 4, 6, 9]
    print(sorted(list1))
    employee1 = Employee('Stefan', 'Developer', 5000)
    employee2 = Employee('Jan', 'Tester', 4000)
    employee3 = Employee('Zenon', 'Tester', 3500)
    employees: typing.List[Employee] = [employee1, employee2, employee3]
    print(sorted(employees, key=lambda employee: employee.salary, reverse=True))
    print(sorted(employees, key=lambda employee: (employee.role, employee.name)))
    print('*' * 50)
    print(min(employees, key=lambda employee: employee.salary))
    print(max(employees, key=lambda employee: employee.salary))


    def salary_of_employee(e: Employee) -> int:
        return e.salary


    print(max(employees, key=salary_of_employee))

    print('*' * 50)

    list_1 = [1, 2, 3, 4, 5]
    squared_list_1 = list(map(lambda number: number ** 2, list_1))
    print(squared_list_1)

    filter_list_1 = list(filter(lambda number: not number % 2, squared_list_1))
    filter_list_2 = list(filter(lambda number: number % 2 == 0, squared_list_1))
    print(filter_list_1)
    print(filter_list_2)

    print('*' * 50)

    list_2 = [2, 3, 4, 5, 6]
    squared_list_2 = [number ** 2 for number in list_2]
    print(squared_list_2)
    filter_list_3 = [number for number in squared_list_2 if number % 2 == 0]
    print(filter_list_3)
