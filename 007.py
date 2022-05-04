def isPrime(x):
    if (x % 10) in [0, 2, 4, 5, 6, 8]:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def nthPrime(x):
    primes = []
    i = 0
    while len(primes) < x:
        if isPrime(i) == True:
            primes.append(i)
        i+=1
    return primes[-2]

print(nthPrime(10001))