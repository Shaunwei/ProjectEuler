#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Sum square difference
Problem:The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def get_sum_square_difference(num):
    if num < 0:
        raise Exception('Got unexpected value %d' % num)
        
    sum_square = sum(x**2 for x in range(1, num + 1))
    square_sum = sum(x for x in range(1, num + 1))**2
    difference = square_sum - sum_square

    return difference



if __name__=='__main__':
    print('test for sum square difference number 10')
    test = get_sum_square_difference(10)
    assert test==2640, 'Should get number 385, got [%d]' % test
    print('Pass Test')
    
    print('sum square difference number 100')
    value = get_sum_square_difference(100)
    print('value is [%d].' % value)
