import numpy

lst = list(map(int, input().split()))

arr = numpy.array(lst)

res = numpy.reshape(arr, (3,3))

print(res)