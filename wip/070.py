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

def divisors(n):
    divisors = [n]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors += [i, int(n/i)]
    return set(divisors)

def totient(n):
    nDivisors = divisors(n)
    coprimesCount = n
    for d in nDivisors:
        if isPrime(d):
            coprimesCount *= ((d-1)/d)
    return int(coprimesCount)

def isPermutation(m, n):
    m = [int(d) for d in str(m)]
    n = [int(d) for d in str(n)]
    if len(m) != len(n):
        return False
    else:
        return sorted(m) == sorted(n)

n = 10**5
while True:
    # print(n)
    # if isPrime(n):
    #     phi = totient(n)
    #     if isPermutation(n, phi):
    #         break
    if isPermutation(n, totient(n)):
        break
    n -= 1
print(n)