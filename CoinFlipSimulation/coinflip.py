"""
Name: coinflip
Purpose: Write some code that simulates flipping a single coin however many times the user decides.
         The code should record the outcomes and count the number of tails and heads
Author: Bruno Albuquerque
Date: 03/01/2022
"""
import random

#Function that validates number of launches
def num_launches():
    while True:
        try:
            i = int(input('How many coin launches? '))
            if i > 0:
                break
            else:
                print('Invalid input. Please try again.')
        except:
            print('Invalid input. Please try again.')
    return i


#Function that simulate coin launch
def coin_launch():
    res = random.choice(['heads', 'tails'])
    return res

#Function that simulate game
def game(i):
    outcome = []
    heads = 0
    tails = 0
    while i > 0:
        res = coin_launch()
        outcome.append(res)
        if res == 'heads':
            heads += 1
        else:
            tails +=1
        i -=1
    print(f'Results: {outcome}')
    print(f'No of Heads: {heads}')
    print(f'No of Tails: {tails}')

#Implementation
if __name__ == '__main__':
    game(num_launches())