def largest_prime_factor(n):
    d = 2
    while d != n:
        if (n % d == 0):
            # Recurse on n without smallest prime factor
            return largest_prime_factor(n // d)
        else:
            d += 1
    # If d == n, only the largest prime factor is left
    return n

print(largest_prime_factor(600851475143))