def left_binary_search(key, numbers):
    left = -1
    rigth = len(numbers) - 1
    while left + 1 < rigth:
        mid = left + (rigth - left) // 2
        if numbers[mid] < key:
            left = mid
        else: rigth = mid
    if numbers[rigth] == key:
        return rigth
    else: return -1


def rigth_binary_search(key, numbers):
    left = 0
    rigth = len(numbers)
    while left + 1 < rigth:
        mid = left + (rigth - left) // 2
        if numbers[mid] <= key:
            left = mid
        else: rigth = mid
    if numbers[left] == key:
        return left
    else: return -1


def main():
    numbers = list(map(int, input("Введити N упорядоченных по неубыванию целых чисел: ").split()))
    key = int(input("Введите значение ключа: "))
    left = left_binary_search(key, numbers)
    rigth = rigth_binary_search(key, numbers)
    if 0 <= left and 0 <= rigth:
        return len(numbers[left : rigth + 1])
    else: return f'{key} - нет в массиве'

if __name__ == '__main__':
    print(main())
