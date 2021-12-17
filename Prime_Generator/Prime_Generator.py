"""
Name: Prime_Generator
Purpose: Generate prime numbers as per user request
Author: Bruno Albuquerque
Date: 17/12/2021
"""

# Function that verifies if a number is prime or not and generates them sequentially
def primes():
    i = 1
    while True:
        flag = True
        if i>=3:
            for j in range(2, i):
                if i%j == 0:
                    flag = False
                    break
        if flag:
            yield i
        i += 1

# Function that receives user input to keep generating prime number or stop
def prime_generator():
    gen = primes()
    while True:
        n = input('Enter for next prime or s for stopping: ')
        print(next(gen))
        if n == 's':
            break

prime_generator()