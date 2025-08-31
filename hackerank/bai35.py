n = int(input())

A = set(map(int, input().split()))

m = int(input())

for i in range(m):
    cmd = input().split()
    op = cmd[0]
    tmp = set(map(int, input().split()))

    if op == "intersection_update":
        A.intersection_update(tmp)
    elif op == "update":
        A.update(tmp)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(tmp)
    elif op == "difference_update":
        A.difference_update(tmp)

print(sum(A))