import numpy

n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
res = numpy.sum(a, axis = 0)
print(numpy.prod(res))
