from collections import Counter

x = int(input())

arr = list(map(int, input().split()))
cnt = Counter(arr)
n = int(input())

sum = 0
for i in range(n):
    size, price = map(int, input().split())
    if cnt[size] > 0 :
        sum += price
        cnt[size] -= 1

print(sum)
