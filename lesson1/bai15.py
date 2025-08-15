def tong(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

print(tong(lst))