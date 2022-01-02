"""
Name: Factorial
Purpose: The factorial of a positive integer n is defined as the product of the sequence , n-1, n-2, ...1 and
        the factorial of 0 is defined as being 1. Solve this using both loops and recursion.
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Function to ask user for the wanted factorial and validate it
def val_input():
    while True:
        try:
            i = int(input('Please introduce the factorial: '))
            if i >= 0:
                break
            else:
                print('Invalid Input. Please try again.')
        except:
            print('Invalid Input. Please try again.')
    return i

#Calculates factorial using recursion
def rec_factorial(n):
    if n == 1:
        return n
    else:
        return n * rec_factorial(n-1)

#Calculates factorial using iteration
def ite_factorial(n):
    factorial = 1
    while n>=1:
        factorial *=n
        n-=1
    return factorial

#Implementation of factorial functions
if __name__ == '__main__':
    i = val_input()
    print(f'By iterative algorithms: {ite_factorial(i)}')
    print(f'By recursive algorithms: {rec_factorial(i)}')

