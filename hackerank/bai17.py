import cmath
z = complex(input().strip())

r = abs(z)
p = cmath.phase(z)

print(r)
print(p)