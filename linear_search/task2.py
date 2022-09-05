def linear_search(arr, key):
    count = 0
    indexes = []
    for i in range(len(arr)):
        if arr[i] == key:
            indexes.append(i+1)
    return print(*indexes)

def main():
    arr = list(map(int, input("Введите массив разделя знаки пробелом: ").split()))
    key = int(input("Введите значение для поиска: "))
    linear_search(arr, key)

if __name__ == '__main__':
    main()