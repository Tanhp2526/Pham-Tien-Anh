import numpy

n = int(input())
a = []
for i in range(n):
    a.append(list(map(float, input().split())))
    
res = numpy.linalg.det(a)

print(round(res, 2))
    