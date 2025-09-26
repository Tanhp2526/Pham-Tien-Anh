s = input()
ok1 = False
ok2 = False
ok3 = False
ok4 = False
ok5 = False
for c in s:
    if c.isalnum():
        ok1 = True
    if c.isalpha():
        ok2 = True
    if c.isdigit():
        ok3 = True
    if c.islower():
        ok4 = True
    if c.isupper():
        ok5 = True

print(ok1)
print(ok2)
print(ok3)
print(ok4)
print(ok5)
    