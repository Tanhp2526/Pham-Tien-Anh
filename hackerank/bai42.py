n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

res = A.symmetric_difference(B)
for i in sorted(res):
    print(i)