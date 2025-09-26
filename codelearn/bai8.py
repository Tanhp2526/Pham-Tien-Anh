n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))
sum = 0
for i in lst:
    sum += i
print(sum)