"""
Name: e_N_Digit
Purpose: Get the value of Euler Number to the Nth digit
Author: Bruno Albuquerque
Date: 15/12/2021
"""

#Function to validate the input (wanted precision) as an integer.
def val_input():
    while True:
        try:
            n = int(input('Enter the number of decimal places for e: '))
            break
        except:
            print('Invalid input. Please enter an integer.')
    return n

#Define function to calculate factorial of a number.
def my_factorial(n):
    res = 1
    i = n
    while i > 0:
        res *=i
        i -= 1
    return res

#Function that implements the calculation of e .
def calc_e(nprec):
    i = 1
    e = 1*10**(nprec+3)
    while True:
        e_old = e
        e += (int(1 * 10**(nprec+3) // my_factorial(i)))
        if abs(e_old-e) < 10**-nprec:
            break
        i += 1
    return str(e)[0] + '.' + str(e)[1:nprec+1]

n = val_input()
print(calc_e(n))