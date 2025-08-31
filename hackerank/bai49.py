from itertools import permutations
s, k = input().split()
k = int(k) 

res = list(permutations(s,k))
res1 = sorted(res)
lst = []
for i in res1:
    tmp = ''.join(i)
    lst.append(tmp)

for i in lst:
    print(i)
 