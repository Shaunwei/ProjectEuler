#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Largest palindrome product
Problem:A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def get_palindrom_number(digit):
    largest_num = 1
    if digit <= 0:
        raise Exception('Wrong Input for digits.')
    while digit > 0:
        largest_num *= 10
        digit -= 1
    else:
        smallest_num = largest_num / 10

    max_product = 0
    valuse = []
    for x in xrange(smallest_num, largest_num):
        for y in xrange(smallest_num, largest_num):
            product = x * y
            if product > max_product:
                if is_palindrom(product):
                    values = [x, y]
                    max_product = product
                else:
                    pass
            else:
                pass

    return values

def is_palindrom(num):
    string = str(num)
    length = len(string)
    for x in range(length/2 + 1):
        head = x
        tail = length - x - 1
        if string[head] != string[tail]:
            return False
    return True

if __name__=='__main__':
    print('test 2-digit number: 9009=91x99')
    test = get_palindrom_number(2)
    expected = 9009
    assert expected==test[0]*test[1], 'Should get 9009, got %s * %s' % (test[0], test[1],)
    print('Pass Test')

    print('find the largest palindrom number for digit 3.')
    value = get_palindrom_number(3)
    print(value)
    print('product is %d.' % (value[0] * value[1],))
