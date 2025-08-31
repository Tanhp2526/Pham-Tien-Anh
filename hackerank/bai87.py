import numpy
numpy.set_printoptions(legacy='1.13')
n,m = map(int, input().split())

res = numpy.eye(n, m, k = 0)
print(res)

