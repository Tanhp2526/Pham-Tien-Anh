n = int(input())

lst = []
for i in range(n):
    name = input()
    diem = float(input())
    lst.append([name,diem])

score = []
for x in lst:
    score.append(x[1])
res = list(set(score))
res.sort()
res2 = res[1]

a = []
for x in lst:
    if x[1] == res2:
        a.append(x[0]) 
a.sort()

for v in a:
    print(v)