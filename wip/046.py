squares = []
primes = []
goldbachs = []
exceptions = []
oddExceptions = []

def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

for i in range(50):
    squares.append(i**2)
for i in range(10000):
    if isPrime(i) == True:
        primes.append(i)

for i in primes:
    for j in squares:
        goldbach = i + 2*j
        if goldbach not in goldbachs:
            goldbachs.append(goldbach)
goldbachs.sort()

for i in range(max(goldbachs)+1):
    if i not in goldbachs:
        exceptions.append(i)

for i in exceptions:
    if i % 2 != 0:
        oddExceptions.append(i)

for i in oddExceptions:
    if isPrime(i) == False:
        print(i)