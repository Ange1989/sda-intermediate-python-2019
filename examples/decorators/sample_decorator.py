import functools


def simple_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f'Decorated -- {func(*args, **kwargs)} -- Decorated'

    return wrapper


@simple_decorator
def hello():
    return 'Hello'


@simple_decorator
def hello_name(name):
    return f'Hello {name}'


# hello = simple_decorator(hello) == @simple_decorator


if __name__ == '__main__':
    # print(hello.__name__)
    print(hello())
    # print(simple_decorator(hello)())
    print(hello_name('Ania'))
    print('*' * 20)
    print(hello.__name__)
    print(hello_name.__name__)
"""
najpierw wywołujemy dekorator simple_decorator, następnie definicja hello wywołuje nam 'Hello', które staje się naszym
func w definicji simple_decorator.


dekoratory zmieniają działanie funkcji
"""
