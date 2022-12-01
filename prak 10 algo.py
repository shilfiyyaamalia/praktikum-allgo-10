# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:37:13 2022

@author: shilaa
"""

def change(p,i,j):
 t = p[i]
 p[i] = p[j]
 p[j] = t
def bubble_sort(p,n):
 for i in range (n-1):
    if p[i] > p[i+1]:
       change(p,i,i+1)
    if n - 1 > 1:
       bubble_sort(p,n-1)
       
       
p= [8,10,6,50,-2,44]
bubble_sort(p, len(p))
print("List yang sudah disorting")
print(p)
