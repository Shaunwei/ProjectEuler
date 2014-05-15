#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Special Pythagorean triplet
Problem:A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def get_pythagorean_numbers(num):
    for a in range(num/3):
        for b in range(a + 1, num/2):
            c = num - a - b
            if a**2 + b**2 == c**2:
                print(a,b,c)
                return a*b*c
    return 0

if __name__=='__main__':
    print('for case a + b + c = 1000')
    values = get_pythagorean_numbers(1000)
    print(values)

