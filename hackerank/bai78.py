import email.utils
import re

s1 = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

t = int(input())
for i in range(t):
    s = input().strip()

    ten, mien = email.utils.parseaddr(s)

    if s1.match(mien):
        print(email.utils.formataddr((ten, mien)))

