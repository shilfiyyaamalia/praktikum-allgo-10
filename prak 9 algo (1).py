# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:28:44 2022

@author: shilaaa


"""

def BinarySearch (arr, low, high, x):
    while (low <= high):
        mid = (low + high)//2
        if arr [mid] == x :
            return mid
        elif arr [mid] < x :
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
arr = [0,11,15,13,22,14,16,37,38,49]
x = int(input("Masukkan Angka : "))
hasil = BinarySearch(arr, 0, len(arr)-1, x)

if hasil != -1:
    print ("Binary dari", x, "adalah di %d" % hasil)
else:
    print("NOT FOUND")