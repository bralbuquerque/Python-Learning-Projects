"""
Name: Bin_Dec
Purpose: Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent
Author: Bruno Albuquerque
Date: 18/12/2021
"""

# Function to ask the user to choose between converters
def converter():
    while True:
        try:
            opt = int(input('Select an option: 1 - Binary to Decimal or 2 - Decimal to Binary: '))
            if opt == 1 or opt ==2:
                break
            else:
                print('Invalid Choice. Please try again.')
        except:
            print('Invalid Choice. Please try again.')
    return opt

# Function to ask the user for the binary number to be converter and validate it as a binary number
def val_binary():
    while True:
        flag = False
        bin_number = input('Please enter the binary number to convert: ')
        bin_str = str(bin_number)
        for i in bin_str:
            if i not in ['0', '1']:
                print('Invalid binary number. Please Try again')
                flag = True
                break
        if not flag:
            return bin_number

# Function to ask the user for the decimal number to be converter and validate it as a decimal number
def val_dec():
    while True:
        try:
            dec_number = int(input('Please enter the decimal number to convert: '))
            break
        except:
            print('Invalid decimal number. Please Try again')

    return dec_number

# Function to convert a binary number to decimal number
def bin_to_dec(bin_number):
    bin_str = str(bin_number)
    i = len(bin_str)-1
    j = 0
    dec = 0
    while i >=0:
        dec += int(bin_str[i]) * 2 ** j
        i -= 1
        j += 1
    print(f'{bin_number} -> {dec}')
    return dec

# Function to convert a decimal number to binary number
def dec_to_bin(dec_number):
    number = dec_number
    bin = []
    bin_str = ''
    while dec_number >= 1:
        reminder = dec_number % 2
        bin.insert(0, reminder)
        dec_number //= 2

    for bit in bin:
        bin_str += str(bit)
    print(f'{number} -> {bin_str}')
    return bin_str

# Converter Implementation
opt = converter()
if opt == 1:
    bin_to_dec(val_binary())
else:
    dec_to_bin(val_dec())

