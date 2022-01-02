"""
Name: Distance Between Two Cities
Purpose: Calculates the distance between two cities and allows the user to specify a unit of distance.
         This program may require finding coordinates for the cities like latitude and longitude
Author: Bruno Albuquerque
Date: 02/01/2022
"""

from geopy.geocoders import Nominatim
import math

geolocator = Nominatim(user_agent="GetLoc")

# Function to get the coordinates of the location 1 and location 2
def get_locations():
    loc1 = input('Introduce the name of the first city: ')
    location1 = geolocator.geocode(loc1)
    print(location1.address)
    coord1 = (location1.latitude, location1.longitude)
    print(location1.latitude, location1.longitude)

    loc2 = input('Introduce the name of the second city: ')
    location2 = geolocator.geocode(loc2)
    print(location2.address)
    coord2 = ((location2.latitude, location2.longitude))
    print(location2.latitude, location2.longitude)

    return (coord1, coord2)

# Function to get the distance between location 1 and location 2 in km using Haversine formula
def haversine(coord):
    lat1_rad = coord[0][0] * math.pi/180
    long1_rad = coord[0][1] * math.pi/180
    lat2_rad = coord[1][0] * math.pi/180
    long2_rad = coord[1][1] * math.pi/180
    a = (math.sin((lat2_rad-lat1_rad)/2))**2 + math.cos(lat1_rad)*math.cos(lat2_rad)*(math.sin((long2_rad-long1_rad)/2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6371 * c
    return d

# Function that asks user for wanted units and make the conversion
def unit_conversion(d):
    print('Select the intended unit:')
    print('1) Km')
    print('2) Miles')
    while True:
        try:
            opt = int(input('Option: '))
            if opt in range(1, 3):
                break
            else:
                print('Invalid Option. Please try again.')
        except:
            print('Invalid Option. Please try again.')

    if opt == 1:
        distance = d
        units = 'km'
    else:
        distance = d * 0.621371192
        units = 'miles'

    return (distance, units)


# Implementation of the calculator
if __name__ == '__main__':
    coord = get_locations()
    d = haversine(coord)
    distance, units = unit_conversion(d)
    print(f'Distance between cities: {distance} {units}')