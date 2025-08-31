k = int(input())

r = list(map(int, input().split()))

c = (sum(set(r))*k - sum(r))//(k-1)

print(c)