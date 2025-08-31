n = int(input())
e = set(map(int, input().split()))

m = int(input())
p = set(map(int, input().split()))

res = e.difference(p)

print(len(res))