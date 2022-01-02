"""
Name: alarm
Purpose: A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
Author: Bruno Albuquerque
Date: 02/01/2022
"""
import re
import datetime
import time

#Function to validate option for Timer/Countdown or Alarm at specific time
def opt():
    while True:
        print('Select an Option:')
        print('1) Timer')
        print('2) Alarm')
        try:
            opt = int(input('Option: '))
            if opt in [1,2]:
                return opt
                break
            else:
                print('Invalid input. Please try again')
        except:
            print('Invalid input. Please try again')

#Function to validate specific time for Alarm
def val_time():
    pattern = '^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
    while True:
            t = input('Please enter the time for the alarm in the following format(HH:MM): ')
            result = re.match(pattern, t)
            if result != None:
                break
            else:
                print('Invalid input. Please try again.')
    return t

#Function to validate time to countdown
def val_timer():
    pattern = '^([0-5][0-9]|[0-9]):[0-5][0-9]$'
    while True:
        t = input('Please enter the timer in the following format(MM:SS): ')
        result = re.match(pattern, t)
        if result != None:
            break
        else:
            print('Invalid input please try again.')
    return t

# Implementation of the Alarm
if __name__ == '__main__':
    o = opt()
    if o == 1:
        t = val_timer()
        time_spit = t.split(':')
        min = int(time_spit[0])*60
        seg = int(time_spit[1])
        dur = min + seg
        while True:
            print(dur)
            time.sleep(1)
            dur -= 1
            if dur == 0:
                print('Done')
                break
    else:
        t = val_time()
        while True:
            now = datetime.datetime.now()
            current_time = now.strftime('%H:%M')
            if current_time == t:
                print('Wake Up')
                break


