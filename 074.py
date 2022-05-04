#Correctly answered 402 when run on Google Colab

import math

def digitFactorialChain(n):
    chain = []
    while True:
        n = [int(i) for i in str(n)]
        for i in range(len(n)):
            n[i] = math.factorial(n[i])
        if sum(n) not in chain:
            n = sum(n)
            chain.append(n)
        else:
            return len(chain)+1

count = 0
for i in range(1000001):
    if digitFactorialChain(i) == 60:
        count += 1
print(count)