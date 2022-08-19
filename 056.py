# 972
# Found answer in 0.1868419647216797 seconds

def digitalSum(a, b):
    return sum([int(i) for i in str(a**b)])

maxDigitalSum = 0

for a in range(1, 100):
    for b in range(1, 100):
        if digitalSum(a, b) > maxDigitalSum:
            maxDigitalSum = digitalSum(a, b)

print(maxDigitalSum)