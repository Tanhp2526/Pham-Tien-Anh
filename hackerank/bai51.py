from itertools import combinations_with_replacement

s,k = input().split()
k = int(k)
s = sorted(s)
for i in combinations_with_replacement(s,k):
    print(''.join(i))