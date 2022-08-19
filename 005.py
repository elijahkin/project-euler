# 232792560
# Found answer in 104.99480199813843 seconds

def evenlyDivisbleForAllSmallerY(x, y):
    for i in range(1, y+1):
        if x % i != 0:
            return False
    return True

for i in range(2520, 232792561):
    if evenlyDivisbleForAllSmallerY(i, 20) == True:
        print(i)
        break