l = 1000000

def divisorSum(n):
    s = 1
    for d in range(2, round(n**0.5)):
        if n % d == 0:
            s += d
            s += n // d
    return s

s = []
for i in range(l):
    s.append(divisorSum(i))

def chain(n):
    i = 1
    x = s[n]
    while True:
        if x != n:
            i += 1
            x = s[x]
            if i > 100:
                return False
        else:
            return i

c = []
for i in range(10000):
    c.append(chain(i))
print(max(c))