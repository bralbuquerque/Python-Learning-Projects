"""
Name: PI_N_Digit
Purpose: Get the value of PI to the Nth digit
Algorithm: Chudnovsky
Author: Bruno Albuquerque
Date: 07/12/2021
"""

#Define function to calculate the square root of an integer, with precision passed in.
def my_sqrt(n, nprec):
    precision = 10**(nprec+3)
    n = n * precision * precision
    x = n
    while True:
        root = (x+n//x)//2
        if abs(root - x) == 0:
            break
        else:
            x = root
    #print(str(x)[0:len(str(x))-nprec] + '.' + str(x)[-nprec:len(str(x))])
    return int(x)

#Function to validate the input (wanted precision) as an integer.
def val_input():
    while True:
        try:
            n = int(input('Enter the number of wanted decimal places of PI: '))
            break
        except:
            print('Error in the value. Please enter an integer.')
    return n

#Function that implements Chudnovsky Algorithm.
def chudnovsky(nprec):
    iter = -(nprec//-14)
    a_k = 10**(nprec+3)
    a_sum = 10 ** (nprec+3)
    b_sum = 0
    for k in range(1, iter):
        a_k *= -(6*k-5) * (2*k-1) * (6*k-1)
        a_k //= k**3 * (640320**3//24)
        a_sum += a_k
        b_sum += k*a_k
    pi = (426880*my_sqrt(10005, nprec)) * 10**nprec // (13591409*a_sum + 545140134*b_sum)
    return str(pi)[0]+'.'+str(pi)[1:]


nprec = val_input()
print(chudnovsky(nprec))
