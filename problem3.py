"""Largest prime factor
Problem:The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    
    if not num%2 or not num%3:
        return False
    
    for i in xrange(5, int(num**0.5) + 1, 6):
        if not num%i or not num%(i + 2):
            return False
    return True

def get_largest_prime(value):
    for x in range(1, int(value**0.5)):
        if not value%x and is_prime(x):
            yield x


if __name__=='__main__':
    print('test 13195')
    test = list(get_largest_prime(13195))
    assert test[-1]==29,'The largest prime of 13195, should be 29, got [%s]' % test
    print(test)
    print('Pass Test')

    print('largest prime factor of number 600851475143')
    value = list(get_largest_prime(600851475143))
    print(value)
