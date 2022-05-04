import math

sum = 0
value = str(math.factorial(100))
for i in range(0, len(value)):
    sum+=int(value[i])
print(sum)