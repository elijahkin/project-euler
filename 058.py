def isPrime(x):
    if x == 2 or x == 5:
        return True
    if (x % 10) in [0, 2, 4, 5, 6, 8] or x == 1:
        return False
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

side_length = 3
prime_count = 0
total_count = 1
base = 1
while True:

    # add each corner
    prime_count += isPrime(base + 1 * (side_length - 1))
    prime_count += isPrime(base + 2 * (side_length - 1))
    prime_count += isPrime(base + 3 * (side_length - 1))
    prime_count += isPrime(base + 4 * (side_length - 1))

    base += 4 * (side_length - 1)
    total_count += 4

    #print('{}: {}/{}'.format(side_length, prime_count, total_count))
    if prime_count < (0.1 * total_count):
        print(side_length)
        break

    side_length += 2