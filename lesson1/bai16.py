def max3(a,b,c):
    max = a
    if(b > max):
        return b
    if(c > max):
        return c
    
a = int(input())
b = int(input())
c = int(input())

print(max3(a,b,c))