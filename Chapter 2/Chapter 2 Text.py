# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:58:53 2022

@author: elena.nardi
"""

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
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
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payement(self, amount):
        self._balance -= amount
   
        
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        
    def charge(self,price):
        succes = super.charge(price)
        if not succes:
            self._balance += 5
        return succes
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._aprt, 1/12)
            self._balance *= monthly_factor
            
if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500))
    wallet.append(CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500))
    wallet.append(CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000))
    
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payement(100)
            print("New balance =", wallet[c].get_balance())
        print()

class Vector:
    def __init__(self, d):
        self._coords = [0]*d
        
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
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"
    
    
class SequenceIterator:
    
    
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1
        
    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()
            
    def __iter__(self):
        return self
    
    
class Range:
    def __init__(self, start, stop = None, step =1):
        if step == 0: 
            raise ValueError("Step cannot be 0")
        if stop is None:
            start, stop = 0, start
            
        self._length = max(0, (stop-start+step-1)//step)
        self._start = start
        self._step = step
        
        
        def __len__(self):
            return self._length
        
        def __getitem__(self, k):
            if k < 0:
                k += len(self)
            if not 0 <= k <= self._length:
                raise IndexError("Index out of range")
            return self._start + k*self._step
            
from abc import ABCMeta, abstractmethod


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        