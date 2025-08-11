import math
def tong(n):
    sum = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if i != n // i:
                sum += i + n // i
            else:
                sum += i
    return sum

n = int(input())
print(tong(n))