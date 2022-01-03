"""
Name: complex_algebra
Purpose: Show addition, multiplication, negation, and inversion of complex numbers in separate functions.
            (Subtraction and division operations can be made with pairs of these operations.)
            Print the results for each operation tested.
Author: Bruno Albuquerque
Date: 03/01/2022
"""
import math

#Implement a class with methods for the multiplication and addition of two complex numbers
class complxope:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return complxnum(self.n1.r + self.n2.r, self.n1.im+self.n2.im).show()

    def mult(self):
        return complxnum(	self.n1.r*self.n2.r-self.n1.im*self.n2.im, self.n2.r*self.n1.im+self.n1.r*self.n2.im).show()

#Implement a class with methods for the definition complex numbers
class complxnum:
    def __init__(self, x, y):
        self.r = x
        self.im = y

    def show(self):
        print(f'{self.r}+{self.im}i')

    def negate(self):
        self.r *= -1
        self.im *= -1
        return self

    def inversion(self):
        root = math.sqrt(self.r*self.r + self.im*self.im)
        self.r = self.r/root
        self.im = -self.im/root
        return self

# Definition of the complex numbers
n1 = complxnum(1, 2)
n2 = complxnum(2, 3)

# Show complex numbers
print('Numbers')
n1.show()
n2.show()

# Negate complex numbers
print('\nNegations')
n1.negate().show()
n2.negate().show()

# Invert complex numbers
print('\nInversions')
n1.inversion().show()
n2.inversion().show()

# Adds complex numbers
print('\nAddition')
c = complxope(n1, n2)
c.add()

# Multiplies complex numbers
print('\nMultiplication')
c.mult()

