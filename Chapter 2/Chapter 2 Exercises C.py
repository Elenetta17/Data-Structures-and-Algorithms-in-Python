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
    
test = ReversedSequenceIterator([1,2,3])
for el in test:
    print (el)