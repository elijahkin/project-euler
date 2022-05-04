import itertools

def permutations(x):
    x = list(itertools.permutations([int(i) for i in str(x)]))
    for i in range(len(x)):
        x[i] = int(''.join(str(j) for j in x[i]))
    return x

def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def countPermutationPrimes(x):
    count = 0
    stinky = permutations(x)
    for i in stinky:
        if isPrime(i) == True:
            count += 1
    return count

print(countPermutationPrimes(1444))