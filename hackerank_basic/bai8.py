n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

max1 = -1e9
max2 = -1e9

for i in lst:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1 :
        max2 = i

print(max2)