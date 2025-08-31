def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lst = []

    for i in range(size):
        l = alpha[size-1 : size-i-1 : -1]
        r = alpha[size-i-1 : size]
        row = "-".join(l+r)
        lst.append(row.center(4*size-3, "-"))

    print("\n".join(lst + lst[-2::-1]))
n = int(input())
print_rangoli(n)