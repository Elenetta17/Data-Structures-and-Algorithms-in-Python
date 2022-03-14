# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:07:39 2022

@author: elena
"""
from random import randrange

def is_multiple(n,m):
    if n%m==0:
        return True
    return False

def is_even(k):
    if str(k)[-1] in ["0","2","4", "6", "8"]:
        return True
    return False

def minmax(lst = []):
    if lst:
        minimum = lst[0]
        maximum = lst[0]
        for i in lst:
            if i < minimum:
                minimum =i
            if i > maximum:
                maximum = i
        return minimum, maximum

def sum_squares(n):
    return sum([i**2 for i in range(n) if i%2==0])

def choice(sequence):
    rand = randrange(min(sequence), max(sequence))
    while rand not in sequence:
        rand = randrange(min(sequence), max(sequence))
    return rand
    
    
if __name__== "__main__":   
    print(choice([1,7,8,9,10,2,21,-5,6,8]))
    
    
    