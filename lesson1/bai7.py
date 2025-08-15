a = int(input())
b = int(input())

c = 0
l = 0

for i in range(a,b+1):
    if i % 2 == 0:
        c += 1
    else:
        l += 1

print(c)
print(l)

    