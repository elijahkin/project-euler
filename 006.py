def sumOfSquares(x):
    sumOfSquares = 0
    for i in range(1, x+1):
        sumOfSquares += i**2
    return sumOfSquares

def squareOfSums(x):
    sum = 0
    for i in range(1, x+1):
        sum += i
    return sum**2

def squareSumDifference(x):
    return squareOfSums(x) - sumOfSquares(x)

print(squareSumDifference(100))