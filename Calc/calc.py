"""
Name: calc
Purpose: A simple calculator to do basic operators
Author: Bruno Albuquerque
Date: 18/12/2021
"""
#Function to validate user input (numbers and operation)
def val_input():
    while True:
        flag = False
        try:
            x = float(input('Enter number 1: '))
            y = float(input('Enter number 2: '))
            ope = input('Enter operation (+, -, *, /): ')
            if ope not in ['+', '-', '*', '/']:
                flag = True
                print('Invalid Operation. Please try again.')
            if not flag:
                return (x, y, ope)
        except:
            print('Invalid input. Please try again.')

#Function to perform the calculation in accordance with user input
def calc(operation):
    if operation[2] == '+':
        print(f'{operation[0]} {operation[2]} {operation[1]} = {operation[0]+operation[1]}')
    if operation[2] == '-':
        print(f'{operation[0]} {operation[2]} {operation[1]} = {operation[0]-operation[1]}')
    if operation[2] == '*':
        print(f'{operation[0]} {operation[2]} {operation[1]} = {operation[0]*operation[1]}')
    if operation[2] == '/':
        print(f'{operation[0]} {operation[2]} {operation[1]} = {operation[0]/operation[1]}')

#Calculator implementation
def main():
    calc(val_input())

if __name__ == '__main__':
    main()