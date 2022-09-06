def left_binary_search(key, numbers):
    
    left = -1
    rigth = len(numbers) - 1
    while left + 1 < rigth:
        mid = left + (rigth - left) // 2
        if numbers[mid] < key:
            left = mid
        else:
            rigth = mid
    if numbers[rigth] == key:
        return rigth + 1
    else: return 0





def main():
    numbers = list(map(int, input("Введити N упорядоченных по неубыванию целых чисел: ").split()))
    keys = list(map(int, input("Введите M целых неотрицательных чисел (ключей для поиска): ").split()))
    for key in keys:
        print(left_binary_search(key, numbers))


if __name__ == '__main__':
    main()