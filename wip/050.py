primes = []

def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

for i in range(100000):
    if isPrime(i) == True:
        primes.append(i)
print(primes)

def consecutivePrimeSum(x):
    sum = 0
    iterations = 0
    while True:
        if (sum + primes[iterations]) < x:
            sum += primes[iterations]
            iterations += 1
        else:
            return sum, iterations

def primeConsecutivePrimeSum(x):
    sum = consecutivePrimeSum(x)[0]
    iterations = consecutivePrimeSum(x)[1]-1
    while True:
        if isPrime(sum) == True:
            return sum
        else:
            sum -= primes[iterations]
            iterations -= 1

print(primeConsecutivePrimeSum(1000))