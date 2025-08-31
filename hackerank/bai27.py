def solve(s):
    tmp = s.split(" ")
    lst = []
    for c in tmp:
        if c:
            if c[0].isalpha():
                lst.append(c[0].upper() + c[1:])
            else:
                lst.append(c)
        else:
            lst.append("")
    return " ".join(lst)

s = input()

result = solve(s)

print(result)
