import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        out = Complex(0, 0)
        out.real = self.real+no.real
        out.imaginary = self.imaginary+no.imaginary
        return out

    def __sub__(self, no):
        out = Complex(0, 0)
        out.real = self.real-no.real
        out.imaginary = self.imaginary-no.imaginary
        return out

    def __mul__(self, no):
        out = Complex(0, 0)
        out.real = self.real*no.real - self.imaginary*no.imaginary
        out.imaginary = self.real*no.imaginary+self.imaginary*no.real
        return out

    def __truediv__(self, no):
        out = Complex(0, 0)
        out.real = (self.real*no.real + self.imaginary*no.imaginary)/(no.real**2 + no.imaginary**2)
        out.imaginary = (-self.real*no.imaginary+self.imaginary*no.real)/(no.real**2 + no.imaginary**2)
        return out

    def mod(self):
        out = Complex(0, 0)
        out.real = math.sqrt(self.real**2 + self.imaginary**2)
        return out

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

c = map(float, input().split())
d = map(float, input().split())
x = Complex(*c)
y = Complex(*d)
print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
