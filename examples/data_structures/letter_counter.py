from collections import defaultdict, Counter


def count_letters_v1(text: str) -> dict:
    counter = {}
    for letter in text:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    return counter


if __name__ == '__main__':
    print(count_letters_v1("example text"))


def count_letters_v2(text: str) -> dict:
    counter = defaultdict(int)
    for letter in text:
        counter[letter] += 1

    return counter


if __name__ == '__main__':
    print(count_letters_v2("example text"))


def count_letters_v3(text: str) -> dict:
    counter = defaultdict(int)
    for letter in text:
        counter[letter] += 1

    return counter


if __name__ == '__main__':
    print(count_letters_v3("example text"))
    print("*" * 50)
    # workers = {}
    # workers['developers'] = []
    workers = defaultdict(list)
    workers['developers'].append('Bob')

    print(workers)


def count_letters_v4(text: str) -> dict:
    return Counter(text)


if __name__ == '__main__':
    print("*" * 50)
    print(count_letters_v4("example text"))
