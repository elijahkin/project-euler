# -59231
# Found answer in 2.517774820327759 seconds

def isPrime(x):
    if x < 0:
        return False
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

def quadratic_consec_primes(a, b):
    n = 0
    while isPrime(n*n + a*n + b):
        n += 1
    return n

largest_count = 0
largest_count_prod = 0
for a in range(-1000, 1000):
    for b in range(-1001, 1001):
        count = quadratic_consec_primes(a, b)
        if count > largest_count:
            largest_count = count
            largest_count_prod = a * b
print(largest_count_prod)