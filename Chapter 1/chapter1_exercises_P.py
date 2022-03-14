# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:10:03 2022

@author: elena
"""

"""Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once."""
from random import randint
import string

def possible_strings():
    strings = []
    chars = "catdog"
    for a in "catdog":
        for b in chars.replace(a, ""):
            for c in chars.replace(a, "").replace(b, ""):
                for d in chars.replace(a, "").replace(b, "").replace(c, ""):
                    for e in chars.replace(a, "").replace(b, "").replace(c, "").replace(d, ""):
                        for f in chars.replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(e, ""):

                            word = a+b+c+d+e+f
                            print(word)
                        #chars = "catdog"
                        
    return strings

def lessthen2(n):
    i = 0
    while n > 2:
        n = n/2
        i+=1
    return i
    
def handcalc():
    equal = False
    inputs = []
    while equal != True:
        input_key = input()
        number = ""
        if input_key == "clear":
            inputs = []
            number = ""
        if input_key in "+-/+":
            inputs.append(input_key)
        while input_key in "0123456789":
            number += input_key
            input_key = input()
        inputs.append(number)
        inputs.append(input_key)
        if input_key == "=":
            equal = True
            break
    if inputs[1]== "+":
        return float(inputs[0])+float(inputs[2])
    
def punishment():
    s = "I will never spam my friends again."
    for i in range(50):
        s = "I will never spam my friends again."
        casual = False
        while not casual:
            random_number = randint(0, len(s)-1)
            if s[random_number]!= " ":
                casual= True
        letter_num = randint(0, len(string.ascii_lowercase)-1)
        s = s[:random_number] + string.ascii_lowercase[letter_num]+s[random_number+1:]
        print(s)
        
def birthday(n):
    dict_birth = {}
    for i in range(n):
        month = randint(1,12)
        if month == 2:
            day = randint(1, 28)
        elif month in [12,4,6,9]:
            day = randint(1, 30)
        else:
            day = randint(1,31)
            
        if str(day)+"-"+str(month) not in dict_birth:
            dict_birth[str(day)+"-"+str(month)]=1
        else:
            dict_birth[str(day)+"-"+str(month)]+=1
    return dict_birth

print(birthday(500))         
                
        