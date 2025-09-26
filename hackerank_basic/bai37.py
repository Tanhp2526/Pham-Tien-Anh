t = int(input())
for i in range(t):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    if(len(A-B)) == 0:
        print(True)
    else:
        print(False)