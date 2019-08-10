if __name__ == '__main__':
    with open('new_file.txt', 'r') as file:
        print(file.read(3))
        print(file.tell())
        print(file.read(3))
        print(file.seek(2))
        print(file.read(3))
    print('*' * 20)

    with open('new_file.txt', 'r') as file:
        print(file.readline())
    print('*' * 20)

    with open('new_file.txt', 'r') as file:
        for line in file.readlines():
            print(line)
    print('*' * 20)

    with open('new_file.txt', 'r') as file:
        for line in file:
            print(line)