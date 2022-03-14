# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:36:25 2022

@author: elena
"""
import string
from random import randint

def reverse(lst):
    rev = []
    for i in range(-1, -len(lst)-1, -1):
        rev.append(lst[i])
    return rev
        
def swap(lst):
    for i in range(0, len(lst)//2):
        lst[i],lst[-i-1]=lst[-i-1], lst[i]
    return lst
        
def odd_product(lst):
    count = 0
    for i in range(0, len(lst)):
        if lst[i]%2 != 0:
            count += 1
        if count == 2:
            return True
    return False

def distinct(lst):
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]==lst[j]:
                return True
    return False

def comprehension(x):
    return [2*(n)*(n-1)/2 for n in range(1,x)]

def shuffle(lst):
    added = []
    shuffled = []
    while len(shuffled) != len(lst):
        randomint = randint(0, len(lst)-1)
        if randomint not in added:
            added.append(randomint)
            shuffled.append(lst[randomint])
    return shuffled
# print(reverse([3,6,9,8]))

# print(swap([3,6,9,8,5]))

#print(odd_product([8,2,5]))
def reverse_input():
    valid_input = True
    input_list = []
    while valid_input:
        try:
            input_list.append(input("Insert something"))
        except EOFError:
            valid_input = False
            return reverse(input_list)
        

def norm(v,p):
    return (sum([v[i]**p for i in range(len(v))]))**(1/p)
#print(distinct([1,2,3,4,5,5]))
#print(shuffle([1,2,3,4,5,6,7,8,9]))
#print(reverse_input())
print(norm([1,2,3],2))