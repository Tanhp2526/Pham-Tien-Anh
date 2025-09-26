n = int(input())

arr = map(int, input().split())

t = tuple(arr)

print(hash(t))
