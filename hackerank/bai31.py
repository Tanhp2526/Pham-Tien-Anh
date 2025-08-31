n = int(input())
e = set(map(int, input().split()))

m = int(input())
p = set(map(int, input().split()))

res = e.union(p)
print(len(res))