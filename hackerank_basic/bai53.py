from itertools import groupby

s = input().strip()
lst = []
for k, g in groupby(s):
    lst.append(f"({len(list(g))}, {k})")

print(" ".join(lst))

