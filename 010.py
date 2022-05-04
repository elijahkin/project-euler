def isPrime(x):
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def primesBelow(x):
    primes = [2, 5]
    for i in range(x):
        if isPrime(i) == True:
            primes.append(i)
    return primes

print(sum(primesBelow(2000000)))