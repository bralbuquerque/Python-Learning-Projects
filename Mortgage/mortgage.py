"""
Name: mortgage
Purpose: Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
Author: Bruno Albuquerque
Date: 17/12/2021
"""

def inputs():
    while True:
        try:
            load = float(input('Enter the value of the load: '))
            period = int(input('Enter the mortgage term in months: '))
            i = float(input('Enter the interest rate of the load: '))
            data = (load, period, i)
            break
        except:
            print('Invalid input. Please repeat.')
    return data

def mortgage_calc(data):
    month_rate = data[2] / 100 / 12
    month_payment = data[0] * (month_rate * (1+month_rate)**data[1] / ((1+month_rate)**data[1]-1))
    print(f'Your Monthly Payment will be: {month_payment:.2f}')

mortgage_calc(inputs())