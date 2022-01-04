"""
Name: sieveeratos
Purpose: The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so
Algorithm: Sieve of Eratosthenes
Author: Bruno Albuquerque
Date: 04/01/2022
"""

#Function to validate input
def val_input():
    while True:
        try:
            i = int(input('Enter a number until which to find prime numbers: '))
            if i > 0:
                break
            else:
                print('Invalid input. Please try again.')
        except:
            print('Invalid input. Please try again.')
    return i

#Sieve Algorithm
def sieve(n):
    prime = [False]*2 + [True]*(n-1)
    for i in range(2,n+1):
        if prime[i]:
            y = i * 2
            while y <= n:
                prime[y] = False
                y += i
            print(i)


#Implementation
if __name__ == '__main__':
    print(sieve(val_input()))