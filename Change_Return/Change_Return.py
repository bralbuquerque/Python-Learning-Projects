"""
Name: Change_Return
Purpose: The user enters a cost and then the amount of money given.
         The program will figure out the change and the number of quarters, dimes, nickels,
         pennies needed for the change
Author: Bruno Albuquerque
Date: 17/12/2021
"""
import math

def input_man():
    while True:
        try:
            cost = float(input('Introduce the cost: '))
            pay = float(input('Introduce the payment given: '))
            data = (cost, pay)
            break
        except:
            print('Invalid input. Try again.')
    return data

def calc_return(data):
    change = data[1] - data[0]
    n_quarters = 0
    n_dimmes = 0
    n_nickels = 0
    n_pennies = 0
    while change >= 0:
        if change >= 0.25:
            n_quarters = math.floor(change/0.25)
            change = round(change - n_quarters*0.25, 3)

        if change >= 0.1 and change < 0.25:
            n_dimmes = math.floor(change / 0.1)
            change = round(change - n_dimmes * 0.1, 3)

        if change >= 0.05 and change < 0.1:
            n_nickels = math.floor(change / 0.05)
            change = round(change - n_nickels * 0.05, 3)

        if change >= 0.01 and change < 0.05:
            n_pennies = math.floor(change / 0.01)
            change = round(change - n_pennies * 0.01, 3)

        if round(change,3) == 0.00:
            break

    print(f'Return: {data[1] - data[0]:.2f}')
    print(f'Quarters: {n_quarters}')
    print(f'Dimmes: {n_dimmes}')
    print(f'Nickels: {n_nickels}')
    print(f'Pennies: {n_pennies}')


calc_return(input_man())
