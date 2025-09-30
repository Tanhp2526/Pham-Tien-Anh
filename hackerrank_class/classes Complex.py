import math

class Complex(object):
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        denom = no.real**2 + no.imaginary**2
        r = (self.real * no.real + self.imaginary * no.imaginary) / denom
        i = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(r, i)

    def mod(self):
        r = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(r, 0)

    def __str__(self):
        if self.imaginary == 0:
            res = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                res = "0.00+%.2fi" % (self.imaginary)
            else:
                res = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            res = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            res = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return res


c = map(float, input().split())
d = map(float, input().split())
x = Complex(*c)
y = Complex(*d)
print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
