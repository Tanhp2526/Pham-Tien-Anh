n, x = map(int, input().split())
diem = []
for i in range(x):
    s = list(map(float, input().split()))
    diem.append(s)

for v in zip(*diem):
    res = sum(v) / x
    print(round(res, 1))