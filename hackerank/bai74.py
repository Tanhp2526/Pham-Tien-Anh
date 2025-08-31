def check(num):
    s = str(num)
    l = 0 
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

n = int(input())
lst = list(map(int, input().split()))

res1 = []
res2 = []
for i in lst:
    res1.append(i > 0)
    res2.append(check(i))

tmp1 = all(res1)
tmp2 = any(res2)

print(tmp1 and tmp2)
    

