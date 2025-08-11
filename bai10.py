n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

a = []

for i in lst:
    if i % 2 == 1:
        a.append(i)

print(a)