def linear_search(arr, key):
    count = 0
    for i in range(len(arr)):
        if arr[i] == key:
            count += 1
    return print(count)

def main():
    arr = list(map(int, input("Введите массив разделя знаки пробелом: ").split()))
    key = int(input("Введите значение для поиска: "))
    linear_search(arr, key)

if __name__ == '__main__':
    main()