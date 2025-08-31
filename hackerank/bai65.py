from datetime import datetime

def check(t1, t2):
    s = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, s)
    dt2 = datetime.strptime(t2, s)
    res = abs(int((dt1 - dt2).total_seconds()))
    return res

t = int(input())
for i in range(t):
    t1 = input().strip()
    t2 = input().strip()
    print(check(t1,t2))