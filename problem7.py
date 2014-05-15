#!/usr/bin/python
# -*- coding: utf-8 -*-
"""10001st prime
Problem:By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def get_nth_prime(n):
    i = 1
    while n > 0:
        i += 1
        if is_prime(i):
            n -= 1
    else:
        return i

def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
        
    if not num%2 or not num%3:
        return False
        
    for i in range(5, int(num**0.5) + 1, 6):
        if not num%i or not num%(i + 2):
            return False
    return True

if __name__=='__main__':
    print('The 6th prime is 13 [2, 3, 5, 7, 11, 13]')
    test = get_nth_prime(6)
    assert test==13, 'Should be 13, got [%d]' % test
    print('Pass Test')
    
    print('The 10001st prime number')
    value = get_nth_prime(10001)
    print(value)
