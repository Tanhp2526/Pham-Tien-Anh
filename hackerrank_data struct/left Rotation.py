def rotateleft(d, arr):
    return arr[d:] + arr[:d]

n, d = list(map(int, input().split()))
arr = list(map(int, input().split()))

res = rotateleft(d, arr)
print(*res)