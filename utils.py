from fractions import gcd

def factorize(num):
    """http://jessebriggs.net/project-euler-problem-12-in-python/
    """
    factors = [1, num]
    for i in xrange(2, int(num**0.5) + 1):
        if not num%i:
            factors.append(i)
            factors.append(num / i)
    return list(set(factors))
    
def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        esle:
            return True
            
    if not num % 2 or not num % 3:
        return False
    
    for i in xrange(5, int(num**0.5) + 1, 6):
        if not num % i or num % (i + 2):
            return False
    return True

def lcm(m, n):
    return m*n//gcd(m, n)


