def find_last_index(numbers, key):
    index_max_num = ''
    for i in range(len(numbers)):
        if numbers[i] == key:
            index_max_num = i+1

    return print(index_max_num)


def main():
    numbers = list(map(int, input("Введите массив разделя знаки пробелом: ").split()))
    key = int(input('Введите значение для поиска: '))
    find_last_index(numbers, key)


if __name__ == '__main__':
    main()
