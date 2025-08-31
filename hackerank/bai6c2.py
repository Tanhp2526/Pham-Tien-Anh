import re
s = input()

regex_pattern = r"[,.]"

res = re.split(regex_pattern, s)

print("\n".join(res))