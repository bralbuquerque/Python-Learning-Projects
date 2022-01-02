"""
Name: Credit Card Validator
Purpose: Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discover) and
         validates it to make sure that it is a valid number (look into how credit cards use a checksum).
Author: Bruno Albuquerque
Date: 02/01/2022
"""

# Function to ask user for input, checks its validity and returns a list with those same numbers
def cc_num():
    while True:
        try:
            cc = input('Please introduce the Credit Card number to validate:')
            if cc.isdigit():
                break
            else:
                print('Invalid number. Please try again.')
        except:
            print('Invalid number. Please try again.')
    cc_list = []
    for i in range(0, len(cc)):
        cc_list.append(int(cc[i]))
    return cc_list

# Function to validate credit card number based on Luhn Formula
def cc_validation(cc_num):
    cc_num = cc_num[::-1]
    sum = 0
    cc_str=''
    for i in range(0, len(cc_num)):
        if i % 2 != 0:
            cc_num[i] = cc_num[i]*2
    for i in range(0, len(cc_num)):
        cc_str += str(cc_num[i])
    for i in range(0, len(cc_str)):
        sum += int(cc_str[i])
    if sum % 10 == 0:
        status = 'Valid'
    else:
        status = 'Invalid'

    return f'Credit Card is {status}.'

# Credit Card Validator Implementation 
if __name__ == '__main__':
    cc = cc_num()
    print(cc_validation(cc))
