def element_search(key, numbers):
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if key == numbers[mid]:
            return print('YES')
        if key > numbers[mid]:
            start = mid + 1      
        else:
            end = mid - 1
    return print('NO')



def main():
    numbers = list(map(int, input("Введите массив разделяя знаки пробелом: ").split()))
    values = list(map(int, input('Введити значения ключей для поиска разделяя пробелом: ').split()))
    for key in values:
        element_search(key, numbers)

if __name__ == '__main__':
    main()

