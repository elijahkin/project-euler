def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def rotations(x):
    x = [int(i) for i in str(x)]
    rotations = []
    for i in range(len(x)):
        x.insert(0, x[-1])
        x.pop(-1)
        rotations.append(int(''.join(str(j) for j in x)))
    return rotations

def isCircularPrime(x):
    for i in rotations(x):
        if isPrime(i) == False:
            return False
    return True

countCirciularPrimes = 0
for i in range(2, 1000001):
    if isCircularPrime(i) == True:
        countCirciularPrimes += 1
print(countCirciularPrimes)