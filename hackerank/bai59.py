from collections import namedtuple

n = int(input())

tmp = input().split()

sv = namedtuple('sv', tmp)

lst = []

for i in range(n):
    data = input().split()

    student = sv(*data)
    lst.append(student)

sum = 0
for i in lst:
    sum += int(i.MARKS)

res = sum / n

print("{:.2f}".format(res))