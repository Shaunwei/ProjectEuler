#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Summation of primes
Problem:The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
def get_primes(num):
    for i in xrange(1, num + 1):
        if is_prime(i):
            yield i
            
def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        else:
            return True
    
    if not num%2 or not num%3:
        return False
    
    for x in xrange(5, int(num**0.5) + 1, 6):
        if not num%x or not num%(x + 2):
            return False
    return True


if __name__=='__main__':
    print('test: sum of primes below 10 is 17')
    test = sum(get_primes(10))
    assert test==17, 'Should get 17, got %d' % test
    print('Pass Test')
    
    print('primes below 2000 000')
    value = sum(get_primes(2000000))
    print(value)
