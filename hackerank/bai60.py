cube = lambda x: x**3

def fibonacci(n):
    lst = []
    a = 0 
    b = 1
    for i in range(n):
        lst.append(a)
        fn = a + b
        a = b
        b = fn
    return lst

n = int(input())
print(list(map(cube, fibonacci(n))))
