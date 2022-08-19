# 9110846700
# Found answer in 0.055140018463134766 seconds

towerSummation = 0
for i in range(1, 1001):
    towerSummation+=i**i
print(str(towerSummation)[-10:])