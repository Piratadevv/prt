import math


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return (self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return (self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return (self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def equals(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ge__(self, other):
        return math.sqrt(self.real ** 2 + self.imag ** 2) > math.sqrt(other.real ** 2 + other.imag ** 2)

    def __le__(self, other):
        return math.sqrt(self.real ** 2 + self.imag ** 2) < math.sqrt(other.real ** 2 + other.imag ** 2)

    def display(self):
        return self.real, self.imag

cr1 = int(input("give me the real part of the first complex number "))
ci1 = int(input("give me the imaginary part of the first complex number "))

cr2 = int(input("give me the real part of the second complex number ")   )        
ci2 = int(input("give me the imaginary part of the second complex number "))

C1 = Complex(cr1, ci1)
#2.1
C2 = Complex(cr2, ci2)
#5.6

print("First Complex Number is as follows:", C1.display())
print("Second Complex Number is as follows:", C2.display())
print('Addition of two complex Numbers is as follows:', C1.__add__(C2))
print("Subtraction of two Complex Numbers is as follows:", C1.__sub__(C2))
print("Multiplication of two Complex Numbers is as follows:", C1.__mul__(C2))
print("Compare Two Complex Numbers:", C1.equals(C2))
print("Checking if C1 is Greater than C2:", C1.__ge__(C2))
print("Checking if C1 is Less than C2:", C1.__le__(C2))
