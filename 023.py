def isAbundant(x):
    factors = []
    for i in range(1, int(x/2+1)):
        if x % i == 0:
            factors.append(i)
    if sum(factors) > x:
        return True
    else:
        return False

abundant = []
for i in range(28123+1):
    if isAbundant(i):
        abundant.append(i)

ints = set(range(28123+1))
for x in abundant:
    for y in abundant:
        if x + y in ints:
            ints.remove(x + y)

print(sum(ints))