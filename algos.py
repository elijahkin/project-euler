import math

def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

#list = [int(i) for i in string if (i % 2) != 0]

def isPalindromic(x):
    x = str(x)
    for i in range(0, math.floor(len(x)/2)):
        if x[i] != x[-i-1]:
            return False
    return True

def isPermutation(m, n):
    m = [int(d) for d in str(m)]
    n = [int(d) for d in str(n)]
    if len(m) != len(n):
        return False
    else:
        return sorted(m) == sorted(n)

# Returns number of integers < n that are coprime with n
def totient(n):
    pd = primeDivisors(n)
    numCoprimes = n
    for d in pd:
        numCoprimes *= ((d-1)/d)
    return numCoprimes

def eratosthenes(n):
    # Set up dictionary, initialize all numbers as primes
    primes = dict()
    for i in range(2, n+1):
        primes[i] = 1
    # Iterate through primes and remove multiples
    for i in primes:
        factors = range(i, n+1, i)
        for f in factors[1:]:
            primes[f] = 0
    return primes