n,m = map(int, input().split())
lst = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

cnt = 0
for i in lst:
    if i in a:
        cnt += 1
    elif i in b:
        cnt -= 1

print(cnt)
