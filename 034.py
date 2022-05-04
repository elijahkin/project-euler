import math

def digitFactorial(x):
    x = str(x)
    sum = 0
    for i in range(len(x)):
        sum += math.factorial(int(x[i]))
    return sum

sum = 0
for i in range(3, 1000001):
    if digitFactorial(i) == i:
        sum += i
print(sum)