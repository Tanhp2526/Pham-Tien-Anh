import re
import sys
t = int(sys.stdin.readline())
for i in range(t):
    s = sys.stdin.readline().strip()
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")
