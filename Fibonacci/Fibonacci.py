"""
Name: Fibonacci
Purpose: Prints a sequence of N Fibonacci sequence elements
Author: Bruno Albuquerque
Date: 16/12/2021
"""

# Function to calculate the nth element of the Fibonacci sequene recursively
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return (recur_fibo(n-1) + recur_fibo(n-2))

# Validates the number of elements wanted as an integer
def _val_input():
    while True:
        try:
            i = int(input('Enter the number of elements for the Fibonacci sequence: '))
            break
        except:
            print('Invalid input. Please enter an integer.')
    return i

# Gets the number of elements wanted as an integer
i = _val_input()

#Create array consituted by the first n elements of the Fibonacci sequence
fib_sequence =[recur_fibo(n) for n in range(i)]
print(fib_sequence)