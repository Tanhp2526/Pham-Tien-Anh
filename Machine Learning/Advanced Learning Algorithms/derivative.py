from sympy import symbols, diff

J, w = symbols('J,w')
J = w**2
print(J)
dj_dw= diff(J,w)
print(dj_dw.subs([(w,2)]))

