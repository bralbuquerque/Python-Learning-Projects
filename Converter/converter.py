"""
Name: converter
Purpose: Converts various units between one another
Author: Bruno Albuquerque
Date: 18/12/2021
"""


#Function to allow user to choose the units to be converted
def opt():
    while True:
        flag = False
        try:
            print('Select conversion:')
            print('1) Volume (m3 <-> ft3)')
            print('2) Mass (kg <-> lb)')
            print('3) Temperature (C, K, F <-> C, K, F)')
            print('4) Currency (EUR <-> USD)')
            print('5) Quit')
            opt = int(input('Option: '))
            if opt not in range(1, 6):
                print('Invalid option. Please try again')
                flag = True

            if not flag:
                return opt
        except:
            print('Invalid option. Please try again')

#Function to allow user to choose the units of the original temperature
def opt_T():
    while True:
        flag = False
        try:
            print('Select original units:')
            print('1) Celsius')
            print('2) Kelvin')
            print('3) Fahrenheit')
            opt_t = int(input('Option: '))
            if opt_t not in range(1,4):
                print('Invalid option. Please try again')
                flag = True

            if not flag:
                return opt_t
        except:
            print('Invalid option. Please try again')

#Function to allow user to choose the units of the original volume
def opt_V():
    while True:
        flag = False
        try:
            print('Select original units:')
            print('1) m3')
            print('2) ft3')
            opt_v = int(input('Option: '))
            if opt_v not in range(1,3):
                print('Invalid option. Please try again')
                flag = True

            if not flag:
                return opt_v
        except:
            print('Invalid option. Please try again')

#Function to allow user to choose the units of the original mass
def opt_M():
    while True:
        flag = False
        try:
            print('Select original units:')
            print('1) Kg')
            print('2) Lb')
            opt_m = int(input('Option: '))
            if opt_m not in range(1,3):
                print('Invalid option. Please try again')
                flag = True

            if not flag:
                return opt_m
        except:
            print('Invalid option. Please try again')

#Function to allow user to choose the units of the original currency
def opt_C():
    while True:
        flag = False
        try:
            print('Select original units:')
            print('1) USD')
            print('2) EUR')
            opt_c = int(input('Option: '))
            if opt_c not in range(1,3):
                print('Invalid option. Please try again')
                flag = True

            if not flag:
                return opt_c
        except:
            print('Invalid option. Please try again')

#Function to validate inputs
def val_inputs():
    while True:
        try:
            n = float(input('Please introduce to value to be converted: '))
            break
        except:
            print('Invalid input. Please try again')
    return n


#Function to convert volume m3 to ft3
def vol_m_ft(vol):
    return vol * 35.31

#Function to convert volume ft3 to m3
def vol_ft_m(vol):
    return vol / 35.31

#Function to convert mass kg to lb
def mass_kg_lb(mass):
    return mass * 2.20

#Function to convert mass lb to kg
def mass_lb_kg(mass):
    return mass / 2.20

#Function to convert temperature Celsius to Kelvin and Fahrenheit
def temp_C_others(temp):
    K = temp + 273
    F = 9/5 * temp + 32
    return (K, F)

#Function to convert temperature Kelvin to Celsius and Fahrenheit
def temp_K_others(temp):
    C = temp - 273
    F = 9/5 * (temp - 273) + 32
    return (C, F)

#Function to convert temperature Fahrenheit to Celsius and Kelvin
def temp_F_others(temp):
    C = 5/9 * (temp - 32)
    K =  5/9 * (temp - 32) + 273
    return (C, K)

#Function to convert currency (USD-EUR)
def curr_USD_EUR(curr):
    return curr / 0.89

#Function to convert currency (EUR-USD)
def curr_EUR_USD(curr):
    return curr * 0.89

#Implementation of the converter
def main():
    option = opt()
    print('\n\n')
    if option == 1:
       opt_v = opt_V()
       n = val_inputs()
       if opt_v == 1:
           print(f'{n} m3 = {vol_m_ft(n)} ft3')
       else:
           print(f'{n} ft3 = {vol_ft_m(n)} m3')
    elif option == 2:
        opt_m =opt_M()
        n = val_inputs()
        if opt_m == 1:
            print(f'{n} kg = {mass_kg_lb(n)} lb')
        else:
            print(f'{n} lg = {mass_lb_kg(n)} kg')
    elif option == 3:
        opt_t = opt_T()
        n = val_inputs()
        if opt_t == 1:
            print(f'{n} Celsius = {temp_C_others(n)[0]} Kelvin / {temp_C_others(n)[1]} Fahrenheit')
        elif opt_t == 2:
            print(f'{n} Kelvin = {temp_K_others(n)[0]} Celsius / {temp_K_others(n)[1]} Fahrenheit')
        else:
            print(f'{n} Fahrenheit = {temp_F_others(n)[0]} Celsius / {temp_C_others(n)[1]} Kelvin')
    elif option == 4:
        opt_c = opt_C()
        n = val_inputs()
        if opt_c == 1:
            print(f'{n} USD = {curr_USD_EUR(n)} EUR')
        else:
            print(f'{n} EUR = {curr_EUR_USD(n)} USD')
    else:
        print('Goodbye')
        return 0

if __name__ == '__main__':
    main()

