def average(arry):
    tmp = set(arry)

    res = sum(tmp) / len(tmp)

    kq = round(res,3)

    return kq

n = int(input())
m = input().split()
arr = list(map(int, m))
a = average(arr)
print(a)
