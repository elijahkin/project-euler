# 31626
# Found answer in 0.13495516777038574 seconds

def d(n):
    divisors = [1]
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return sum(divisors)

sumAmicableNumbers = 0
for i in range(10001):
    if d(d(i)) == i:
        if d(i) != i:
            sumAmicableNumbers += i
print(sumAmicableNumbers)