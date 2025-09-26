n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

res1 = A.union(B)
res2 = A.intersection(B)
res = res1 - res2
tmp = sorted(res)
for x in tmp:
    print(x)