def isPandigital(x):
    digits = [int(i) for i in str(x)]
    for i in range(1, len(digits)+1):
        if i not in digits:
            return False
    return True

def isPrime(x):
    if (x % 10) in [0, 2, 4, 5, 6, 8]:
        return False
    for i in range(2, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

for i in range(1, 987654321):
    if isPandigital(i) == True:
        if isPrime(i) == True:
            print(i)