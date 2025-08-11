def check(lst):
    a = []
    for i in lst:
        if i not in a:
            a.append(i)
    return a

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(check(lst))