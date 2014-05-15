#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Smallest multiple
Problem:2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# LCM(A, B) = (A * B) / GCD(A * B)
# GCD(A, B) = GCD(B, A mod B)
# http://stackoverflow.com/questions/19348430/project-euler-getting-smallest-multiple-in-python

from fractions import gcd
from functools import reduce

def get_smallest_positive_number(num):
    return reduce(lcm, range(1, num + 1))

def lcm(m, n):
    """Calculate the lowest common multiple of two integers m and n
    """
    return m*n//gcd(m, n)

#Wrong thinking
def get_primes_in_num(num):
    for i in xrange(2, num + 1):
        if is_prime(i):
            yield i
        else:
            pass

#Wrong thinking
def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        else:
            return True
    else:
        pass
    
    if not num%2 or not num%3:
        return False
    else:
        pass
        
    for i in xrange(5, int(num**0.5) + 1, 6):
        if not num%i or not num%(i + 2):
            return False
        else:
            pass
    return True



if __name__=='__main__':
    print('test: the smallest positive number from 1 to 10 is 2520')
    test = get_smallest_positive_number(10)
    assert test==2520, 'Should be 2520, got [%d]' % test
    print('Pass Test.')
    
    print('The smallest positive number from 1 to 20 is:')
    value = get_smallest_positive_number(20)
    print(value)
