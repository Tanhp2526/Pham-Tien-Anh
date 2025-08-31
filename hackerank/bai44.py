import math

ab = int(input())
bc = int(input())

res = math.degrees(math.atan2(ab,bc))

print(str(round(res)) + chr(176))