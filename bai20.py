n = int(input())
res = []
for i in range(n):
    res.append(int(input()))
a = []    
for i in res:
    if i % 2 == 0:
        a.append(i)

print(a)