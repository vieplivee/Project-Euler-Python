import math
from collections import defaultdict

def isPrime(n):
    return not [i for i in range(2, int(math.sqrt(n)) + 1) if n%i == 0]

def getAllPrimeFactors(n):
    d = defaultdict(int)
    if n <= 1:
        return d
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime(i) and n%i == 0:
                d = getAllPrimeFactors(n/i)
                d[i] += 1
                return d
        else:
            d[n] += 1
            return d

def combinePrimeFactors(d1, d2):
    d = defaultdict(int)
    for key in set(d1.keys()) | set(d2.keys()):
        d[key] = max(d1[key], d2[key])
    return d

def prob5(n):
    factorset = reduce(combinePrimeFactors, 
        [getAllPrimeFactors(i) for i in xrange(1, n + 1)])
    result = 1
    for factor in factorset:
        result *= int(math.pow(factor, factorset[factor]))
    return result

answer5 = prob5 (20)