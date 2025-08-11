n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    for j in range(i):
        if lst[j] > lst[i]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print(lst)