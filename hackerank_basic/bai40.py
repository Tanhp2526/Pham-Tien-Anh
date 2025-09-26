A = set(map(int, input().split()))
n = int(input())
ok = True
for i in range(n):
    s = set(map(int, input().split()))
    if not(A > s):
        ok = False
        break

print(ok)