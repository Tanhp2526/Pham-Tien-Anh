n = int(input())

res = []

for i in range(n):
    res.append(int(input()))

tmp = ""

for x in res:
    tmp = tmp + str(x)

print(tmp)