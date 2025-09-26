import re

s = input()

res = r'[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]([aeiouAEIOU]+)[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]'

tmp = re.findall(res, s)

if tmp:
    for i in tmp:
        print(i)
else:
    print(-1)
