"""
Name: bubblesort
Algorithm: Bubble Sort
Purpose: Arrange array in dondecreasing order
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Function that defines Bubble Sort
def bubble_sort(arr):
    counter = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            print(arr)


arr = [5, 1, 4, 2, 8, 3]
print(arr)
bubble_sort(arr)