# 76576500
# Found answer in 3.1025078296661377 seconds

def triangle(x):
    return int(0.5*(x**2+x))

def countFactors(x):
    countFactors = 0
    for i in range(1, int(x**0.5+1)):
        if x % i == 0:
            countFactors += 1
    return 2*countFactors

for i in range(100000):
    if countFactors(triangle(i)) >= 500:
        print(triangle(i))
        break