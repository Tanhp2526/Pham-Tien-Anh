import math
def tong(n):
    sum = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if i != n // i:
                sum += i + n // i
            else:
                sum += i
    if sum < n :
        return False
    else:
        return True
    
n = int(input())
print(tong(n))