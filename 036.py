# 872187
# Found answer in 0.8918290138244629 seconds

import math

palindromes = []
doubleBasePalindromes = []

def isPalindromic(x):
    x = str(x)
    for i in range(0, math.floor(len(x)/2)):
        if x[i] != x[-i-1]:
            return False
    return True

def toBaseTwo(x):
    return int(''.join(map(str,list(bin(x))[2:])))

for i in range(1000001):
    if isPalindromic(i) == True:
        palindromes.append(i)
for i in palindromes:
    if str(toBaseTwo(i))[0] != '0' and isPalindromic(toBaseTwo(i)) == True:
        doubleBasePalindromes.append(i)
print(sum(doubleBasePalindromes))