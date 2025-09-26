import numpy

n, m = map(int, input().split())

lst = []
for i in range(n):
    s = list(map(int, input().split()))
    lst.append(s)

tmp = numpy.array(lst)

res = tmp.min(axis = 1)

print(res.max())