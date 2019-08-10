# def sum_value(a, b):
#     return a + b
#
#
# def subtract_value(a, b):
#     return a - b
#
#
# s = sum_value
#
#
# def make_operation(operation, a, b):
#     return operation(a, b)


def make_operation2(symbol, a, b):
    def sum_value2(a, b):
        return a + b

    def subtract_value2(a, b):
        return a - b

    if symbol == '+':
        return sum_value2(a, b)
    if symbol == '-':
        return subtract_value2(a, b)
    else:
        raise NotImplementedError()


def get_operation2(symbol):
    def sum_value2(a, b):
        return a + b

    def subtract_value2(a, b):
        return a - b

    if symbol == '+':
        return sum_value2
    if symbol == '-':
        return subtract_value2
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    # print(sum_value(1, 3))
    # print(s(1, 3))

    print('*' * 20)

    # print(make_operation(sum_value, 1, 3))

    print('*' * 20)

    print(make_operation2('-', 1, 3))
    print(make_operation2('+', 1, 3))
    # print(make_operation2('*', 1, 3))

    print('*' * 20)

    print(get_operation2('+')(1, 3))

    sum_ints = get_operation2('+')
    print(sum_ints(1, 3))
