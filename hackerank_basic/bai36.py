t = int(input())

for i in range(t):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    ok = True
    for x in A:
        if x not in B:
            ok = False
            break

    print(ok)