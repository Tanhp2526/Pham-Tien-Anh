import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = list(itertools.product(A,B))

print(res)