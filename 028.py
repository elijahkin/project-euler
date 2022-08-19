# 669171001
# Found answer in 0.04200911521911621 seconds

def diagonalSum(x):
    sum = 1
    for i in range(2, int(0.5*x+1.5)):
        sum += levelSum(i)
    return sum

def levelSum(x):
    return int(16*x**2-28*x+16)

print(diagonalSum(1001))