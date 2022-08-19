# 748317
# Found answer in 3.805327892303467 seconds

def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def isTruncatablePrime(x):
    x = str(x)
    truncates = []
    for i in range(1, len(x)):
        truncates.append(int(x[i:]))
        truncates.append(int(x[:i]))
    truncates.sort()
    for i in truncates:
        if isPrime(i) == False:
            return False
    return True

primes = []
truncatablePrimes = []

for i in range(8, 1000000):
    if isPrime(i) == True:
        primes.append(i)

for i in primes:
    if isTruncatablePrime(i) == True:
        truncatablePrimes.append(i)

print(sum(truncatablePrimes))