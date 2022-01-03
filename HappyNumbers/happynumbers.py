"""
Name: happynumbers
Purpose: A happy number is defined by the following process. Starting with any positive integer,
         replace the number by the sum of the squares of its digits, and repeat the process until
         the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
         Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1
         are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Define function to get the positive integer from the user and validate it and split its digits into a list
def get_numbers():

    while True:
        try:
            num = int(input('Please enter a positive integer to verify as happy number: '))
            if num > 0:
                break
            else:
                print('Negative number. Only positive allowed')
        except:
            print('Invalid input. Please try again')

    return num

# Define function to split a number into its digits on a list
def split_num(num):

    digits = []
    while num:
        digits.append(num % 10)
        num //= 10

    digits.reverse()

    return digits

#Function to verify if number is happy
def happy(digits):
    previous_sums = []
    while True:
        sum_squares = sum(list(map(lambda x : x**2 , digits)))
        if sum_squares == 1:
            return True
        elif sum_squares in previous_sums:
            return False
        else:
            num = sum_squares
            previous_sums.append(num)
            digits = split_num(num)

#Function to print 8 first happy numbers
def happy_numbers():
    happy_numbers = []
    num = 1
    while len(happy_numbers) <= 7:
        dig = split_num(num)
        if happy(dig):
            happy_numbers.append(num)
        num += 1
    return happy_numbers



print(happy_numbers())
