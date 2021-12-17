"""
Name: cost_of_tiles
Purpose: Calculate the total cost of tile it would take to cover a floor plan of width and length,
         using a data entered by the user
Author: Bruno Albuquerque
Date: 17/12/2021
"""

#Function to validate the input as a number.
def val_input():
    while True:
        try:
            c = float(input('Enter the cost per tile: '))
            l = float(input('Enter the length of the floor: '))
            w = float(input('Enter the width of the floor: '))
            data = (c, l, w)
            break
        except:
            print('Invalid input. Please enter an integer.')
    return data

#Function to calculate the total cost of tiles and print it.
def calc(data):
    price = data[0] * data[1] * data[2]
    print(f'The total price to cover a {data[1]} x {data[2]} floor is {price}')

calc(val_input())