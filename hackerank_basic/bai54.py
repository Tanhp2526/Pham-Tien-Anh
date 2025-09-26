from itertools import combinations
n = int(input().strip())
s = input().split()
k = int(input().strip())

c = list(combinations(s,k))
cnt = 0
for i in c:
    if 'a' in i:
        cnt += 1

xs = cnt / len(c)

print(round(xs, 3))

        
