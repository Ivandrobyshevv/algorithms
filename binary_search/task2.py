from math import log2, ceil
num = int(input())
numbers = [i for i in range(1, num+1)]
start = 0
end = len(numbers) - 1
count = 0 
while start <= end:
    mid = (start + end) // 2
    if num > numbers[mid]:
        count += 1
        start = mid + 1      
    else:
        count += 1
        end = mid - 1
print(count)


print(ceil(log2(num)))
print(ceil(log2(int(input()))))