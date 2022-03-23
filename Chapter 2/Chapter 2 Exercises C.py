# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:13:17 2022

@author: elena.nardi
"""

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
    
    def __eq__(self, other):
        return self._seq == other._seq
    
    def __lt__(self, other):
        return self._seq < other._seq
    
class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k=0
    
    def __next__(self):
        self._k -= 1
        if abs(self._k) <= len(self._seq):
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
        
        def __contains__(self, n):
            if not 0 <= n <= self._length: 
                raise IndexError("Index out of range")
                
            if (n - self._start) % step == 0:
                return True
            else:
                return False
            
            
class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._totalamount = 0
        
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
        self._totalamount += amount
        self._balance -= amount
   
        
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, minmonth):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._charge_count = 0
        self._minmonth = minmonth
        self._minimum = self._balance*self._minmonth/100

        
    def charge(self,price):
        succes = super().charge(price)
        self._charge_count += 1
        if self._charge_count > 10:
            self._balance += 1
        if not succes:
            self._balance += 5
        return succes
    
    def process_month(self):
        self._minimum = self._balance*self._minmonth/100
        if self._balance > 0:
            monthly_factor = pow(1+self._aprt, 1/12)
            self._balance *= monthly_factor
        if self._minimum > self._totalamount :
            self._balance += 10
    
class Progression:
    def __init__(self, start = 0):
        self._current = start
        
    
    def _advance(self):
        self._current += 1
        
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
        
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(" ".join(str(next(self)) for j in range(n)))
        
        
        
class Progression231(Progression):
    def __init__(self, first = 2, second = 200):
        super().__init__(first)
        self._prev = abs(second + first)
        
    def _advance(self):
        self._prev, self._current = self._current, abs(self._current - self._prev)
        
        
class SquareRootProgression(Progression):
    def __init__(self, start = 65536):
        super().__init__(start)
        
    def _advance(self):
        self._current = self._current**0.5 
        
p231 = SquareRootProgression()
p231.print_progression(10)