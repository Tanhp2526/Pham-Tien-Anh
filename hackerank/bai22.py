n = int(input())
c = 'H'

for i in range(n):
    l = (c*i).rjust(n-1)
    m = c
    r = (c*i).ljust(n-1)
    line = l + m + r
    print(line)

for i in range(n+1):
    l = (c*n).center(n*2)
    r = (c*n).center(n*6)
    line = l + r
    print(line)

for i in range((n+1)//2):
    m = (c*n*5).center(n*6)
    print(m)

for i in range(n+1):
    l = (c*n).center(n*2)
    r = (c*n).center(n*6)
    line = l + r
    print(line)

for i in range(n):
    l = (c*(n-i-1)).rjust(n)
    m = c
    r = (c*(n-i-1)).ljust(n)
    line = l + m + r
    print(line.rjust(n*6))
