def swap_case(s):
    res = ""
    for c in s:
        if c.islower():
            res += c.upper()
        elif c.isupper():
            res += c.lower()
        else:
            res += c
    return res
    
s = input()
print(swap_case(s))