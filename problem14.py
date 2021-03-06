#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'shaunwei'
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

MAX_NUMBER = 1000000  # one million


def get_chain_from(num):
    chain = 0
    while num != 1:
        chain += 1
        if num % 2 == 0:  # num is even
            num /= 2
        else:  # num is odd
            num = 3 * num + 1
    return chain


if __name__ == '__main__':
    max_chain = 0
    starter = 0
    for n in range(2, MAX_NUMBER):
        chain = get_chain_from(n)
        if chain > max_chain:
            max_chain = chain
            starter = n
    else:
        print('The number with the longest chain %d' % starter)
