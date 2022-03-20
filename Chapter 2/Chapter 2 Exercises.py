# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:13:11 2022

@author: elena.nardi
"""

class Flower():
    def __init__(self, flower = "", petals = 0, price = 0.0):
        self.flower = flower
        self.petals = petals
        self.price = price
        
        
    def _setflower(self, flower):
        self.flower = flower
        
    def _setpetals(self, petals):
        self.petals = petals
        
            
    def _setprice(self, price):
        self.price = price
        
    def _getflower(self):
        return self.flower
    
    def _getpetals(self):
        return self.petals
    
    def _getprice(self):
        return self.price
    
class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if type(price) is float or type(price) is int:
        
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        else:
            raise TypeError("price must be a number")
            
    def make_payement(self, amount):
        if type(amount) is float or type(amount) is int:
            if amount < 0:
                raise ValueError("Amount must be a positive number")
            self._balance -= amount  
        else:
            raise TypeError("price must be a number")
            
class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0]*d
        else:
            self._coords = d
            # for j in len(self._coords):
            #     self._coords[j]=d[j]
        
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]-other[j]
        return result
    
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=-self[j]
        return result
    
    def __mul__(self,other):
        if isinstance(other, (int, float)):
            result = Vector((len(self)))
            for j in range(len(self)):
                result[j]=self[j]*other
            return result
    
        if isinstance(other, (Vector, list)):
            print(True)
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            result = 0
            print(self,other)
            for j in range(len(self)):
                result+=self[j]*other[j]
            return result
    
    def __rmul__(self, n):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j]*n
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"
            

if __name__=="__main__":
    
    # rose = Flower("rose", 1, 2)
    # print(rose.petals)
    # rose._setpetals(4)
    # print(rose._getpetals)
    # card = CreditCard("Elena", "BNP", "17", 10000, 50)
    # print(card._balance)
    # print(card.get_limit())
    # print(card.make_payement(-1.25))
    
    # wallet = []
    # wallet.append(CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500))
    # wallet.append(CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500))
    # wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000))
    

    # val = 1
    # while wallet[0].charge(val) and wallet[1].charge(2*val) and wallet[2].charge(3*val): 
    #     print(wallet[0].get_balance(), wallet[1].get_balance(), wallet[2].get_balance())
    #     val += 1
    
    # for c in range(3):
    #     print("Customer =", wallet[c].get_customer())
    #     print("Bank =", wallet[c].get_bank())
    #     print("Account =", wallet[c].get_account())
    #     print("Limit =", wallet[c].get_limit())
    #     print("Balance =", wallet[c].get_balance())
    #     while wallet[c].get_balance() > 100:
    #         wallet[c].make_payement(100)
    #         print("New balance =", wallet[c].get_balance())
    #     print()
    a = Vector([1,2,3])
    a[0]=1

    
    print(a*5)