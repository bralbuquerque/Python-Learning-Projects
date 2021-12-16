"""
Name: Prime_Factor
Purpose: Express a number as a product of prime numbers
Author: Bruno Albuquerque
Date: 16/12/2021
"""
#Function to validate the input for prime factorization as an integer.
def val_input():
    while True:
        try:
            n = int(input('Enter an integer for prime factorization:'))
            break
        except:
            print('Invalid input. Please enter an integer.')
    return n

#Function for prime factorization of n.
def prime_factor(n):
    num = []
    number = n
    i = 2
    while i >= 2 and i <= n:
        flag = False
        if number % i == 0:
            num.append(i)
            number = number / i
            flag = True
        i += 1
        if flag:
            i = 2
    return num


print(prime_factor(val_input()))
