"""
Name: mergesort
Algorithm: Merge Sort
Purpose: Arrange array in dondecreasing order
Author: Bruno Albuquerque
Date: 03/01/2022
"""

#Organize numbers
def merge(L, R):
    output= []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            output.append(L[i])
            i += 1
        else:
            output.append(R[j])
            j += 1
    output.extend(L[i:])
    output.extend(R[j:])
    return output


#Implementation of Merge-Sort
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    L = merge_sort(arr[:n//2])
    R = merge_sort(arr[n//2:])
    return merge(L,R)

arr = [10 , 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(merge_sort(arr))