n ,m = map(int, input().split())

for i in range(1,n,2):
    res = (i * ".|.").center(m,"-")
    print(res)

print("WELCOME".center(m,"-"))

for i in range(n-2,0,-2):
    res = (i * ".|.").center(m,"-")
    print(res)