"""
Name: fastexpon
Purpose: Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Function to validate input
def val_input():
    while True:
        try:
            a = int(input('Enter the base: '))
            b = int(input('Enter the exponent: '))
            break
        except:
            print('Invalid input. Please try again.')
    return (a,b)

#Function to perform exponentiation
def pow(nums):
    a= nums[0]
    b = nums[1]
    print(nums)
    if b == 0:
        return 1
    else:
        temp = pow((a, b/2))
        print(temp)
        if (b % 2) == 0:
            return temp * temp
        else:
            return temp * temp * a

#Implementation
if __name__ == '__main__':
    print(pow(val_input()))