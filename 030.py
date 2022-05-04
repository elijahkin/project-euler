def isFifthPowerDigitSum(x):
    digits = [int(i) for i in str(x)]
    sum = 0
    for i in range(len(digits)):
        sum += digits[i]**5
    if sum == x:
        return True
    return False

fifthPowerDigitSum = []
for i in range(2, 1000001):
    if isFifthPowerDigitSum(i) == True:
        fifthPowerDigitSum.append(i)
print(fifthPowerDigitSum)
print(sum(fifthPowerDigitSum))