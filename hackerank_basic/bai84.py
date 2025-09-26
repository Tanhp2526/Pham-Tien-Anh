import numpy

n, m = map(int, input().split())

lst = []
for i in range(n):
    s = list(map(int, input().split()))
    lst.append(s)
    
tmp = numpy.array(lst)
res1 = numpy.transpose(tmp)
res2 = tmp.flatten()
print(res1)
print(res2)
