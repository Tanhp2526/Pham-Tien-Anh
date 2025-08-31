
from collections import OrderedDict
n = int(input())

danhsach = OrderedDict()

for i in range(n):
    s = input().split()
    items = " ".join(s[:-1])
    price = int(s[-1])

    if items in danhsach:
        danhsach[items] += price
    else:
        danhsach[items] = price

for items, res in danhsach.items():
    print(items, res)