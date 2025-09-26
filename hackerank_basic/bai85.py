import numpy

n,m,p = map(int, input().split())

lst1 = []
lst2 = []
for i in range(n):
    arr1 = list(map(int, input().split()))
    lst1.append(arr1)
    
for x in range(m):
    arr2 = list(map(int, input().split()))
    lst2.append(arr2)
    
tmp1 = numpy.array(lst1)
tmp2 = numpy.array(lst2)

tmp = numpy.concatenate((tmp1, tmp2))
res = numpy.reshape(tmp, (n+m, p))
print(res)
