from itertools import groupby

s = input().strip()

lst = []

for k, g in groupby(s):
    cnt = len(list(g))
    lst.append("(" + str(cnt) + ", " + k + ")")

print(" ".join(lst))