import math

def isPrime(n):
    return not [i for i in range(2, int(math.sqrt(n))) if n%i == 0]

def maxPrimeFactors(n):
    x = [i for i in range(2, int(math.sqrt(n)))
      if isPrime(i) and n%i == 0]
    y = [n/i for i in x if i not in x and isPrime(n/i)]
    return max(sum([x, y], []))

answer3 = maxPrimeFactors(600851475143)