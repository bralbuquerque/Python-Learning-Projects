"""
Name: collatzconjecture
Purpose: Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
         If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Function to validate input
def val_input():
    while True:
        try:
            i = int(input('Please enter a number greater than 0: '))
            if i > 0:
                break
            else:
                print('Invalid Input. Please try again')
        except:
            print('Invalid Input. Please try again')
    return i

#Function to run Collatz Conjecture
def collatz(i):
    if i%2 == 0:
        i /= 2
    else:
        i = 3*i +1
    return i

#Function to count operations
def counter(i):
    counter = 0
    while i != 1:
        i = collatz(i)
        counter += 1
    return counter


#Implementation
if __name__ == '__main__':
    print(f'No of steps = {counter(val_input())}')