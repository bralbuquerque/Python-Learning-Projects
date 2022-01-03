"""
Name: numbernames
Purpose: Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but
         you should support inputs up to at least one million (or the maximum value of your language's default bounded
         integer type, if that's less)
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Define number names
units = [' ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens =  ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#Define Function to get user input on the number to be spelled
def get_input():
    while True:
        try:
            num = int(input('Please enter a number between 0 and 999 999 999: '))
            if num <= 999999999 and num >= 0:
                break
            else:
                print('Invalid Input. Please try again.')
        except:
                print('Invalid Input. Please try again.')

    return num

#Define a function to split a number into a list
def num_list(num):
    num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_list[0] = int((num / 100000000) % 10)
    num_list[1] = int((num / 10000000) % 10)
    num_list[2] = int((num / 1000000) % 10)
    num_list[3] = int((num / 100000) % 10)
    num_list[4] = int((num / 10000) % 10)
    num_list[5] = int((num / 1000) % 10)
    num_list[6] = int((num / 100) % 10)
    num_list[7] = int((num / 10) % 10)
    num_list[8] = int((num / 1) % 10)

    return num_list

#Function to check trailing zeros
def check_zeros(arr):
    if arr[6] != 0:
        return arr[7] == 0 and arr[8] == 0
    elif arr[3] != 0 or arr[4] != 0 or arr[5] != 0:
        return arr [6] and arr[7] == 0 and arr[8] == 0
    elif arr[0] != 0 or arr[1] != 0 or arr[2] != 0:
        return arr [3] and arr[4] == 0 and arr[5] == 0 and arr [6] and arr[7] == 0 and arr[8] == 0

#Defines function to spell the chosen number
def num_to_word(num):
    list = num_list(num)
    word = ''
    if num == 0:
        word = 'zero'
    elif num > 0 and num <=9:
        word = units[num]
    elif num >= 10 and num <=19:
        word = teens[num-10]
    elif num >= 20 and num<100:
        word = tens[list[7]-1] +' '+units[list[8]]
    elif num >=100 and num <= 999:
        word = units[list[6]] + ' ' + 'hundred' + ' '
        if not check_zeros(list):
            word += num_to_word(list[7]*10 + list[8])
    elif num >=1000 and num <= 999999:
        word += num_to_word(list[3]*100 + list[4]*10 + list[5]) + ' ' + 'thousand' + ' '
        if not check_zeros(list):
            word += num_to_word(list[6]*100 + list[7]*10 + list[8])
    elif num >= 1000000 and num <= 999999999:
        word += num_to_word(list[0] * 100 + list[1] * 10 + list[2]) + ' ' + 'million' + ' '
        if not check_zeros(list):
            word += num_to_word(list[3]*100000 + list[4]*10000 + list[5]*1000+ list[6] * 100 + list[7] * 10 + list[8])


    return word


if __name__ == '__main__':
    print(num_to_word(get_input()))



