def primeFactors(n):
    factors = []
    primeFactors = []
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    factors.sort()
    for i in factors:
        if isPrime(i) == True:
            primeFactors.append(i)
    return len(primeFactors)

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True

for i in range(1000001):
    if primeFactors(i) == 4:
        if primeFactors(i+1) == 4:
            if primeFactors(i+2) == 4:
                if primeFactors(i+3) == 4:
                    print(i)