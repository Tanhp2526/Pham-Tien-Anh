s = input()
kitu = ''

for c in s:
    if c.isalnum() and c == kitu:
        print(c)
        break
    kitu = c 
else:
    print(-1)

