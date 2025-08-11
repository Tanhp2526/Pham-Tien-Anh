def check(s):
    cnt1 = 0
    cnt2 = 0
    for c in s:
        if c.isupper():
            cnt1 += 1
        if c.islower():
            cnt2 += 1

    print(cnt1)
    print(cnt2)

s = input()

check(s)