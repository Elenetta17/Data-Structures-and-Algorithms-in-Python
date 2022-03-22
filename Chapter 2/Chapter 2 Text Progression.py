# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:24:53 2022

@author: elena.nardi
"""

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
        
        
    
class ArithmeticProgression(Progression):
    
    def __init__(self, increment = 1, start = 0):
        super().__init__(start)
        self._increment = increment
        
    def _advance(self):
        self._current += self._increment
        
        
class GeometricProgression(Progression):
    def __init__(self, base = 2, start = 1):
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        self._current *= self._base
        
        
class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        self._prev = second-first
        
    def _advance(self):
        self._prev, self._current = self._current, self._current + self._prev
        
        
test = ArithmeticProgression(128,0)
i = 0
while test._current < 2**23:
    print(test._current)
    test._advance()
    i+=1