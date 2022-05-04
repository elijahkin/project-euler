import math
import time

t = time.time()

maxN = 10**6
recordRatio = 0
record = 0

def divisors(n):
    divisors = [n]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors += [i, int(n/i)]
    return set(divisors)


def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def totient(n):
    nDivisors = divisors(n)
    coprimesCount = n
    for d in nDivisors:
        if isPrime(d):
            coprimesCount *= ((d-1)/d)
    return coprimesCount


for n in range(2, maxN):
    ratio = n / totient(n)
    if ratio > recordRatio:
        record = n
        recordRatio = ratio
print(record, recordRatio)

print(time.time() - t)
# old - 177s
# new - 0.05s