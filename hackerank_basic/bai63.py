from collections import defaultdict

n,m = map(int, input().split())

A = defaultdict(list)

for i in range(1,n+1):
    s = input().strip()
    A[s].append(i)

for i in range(m):
    s = input().strip()
    if s in A:
        print(" ".join(map(str, A[s])))
    else:
        print(-1)
