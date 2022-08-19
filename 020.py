# 648
# Found answer in 0.04575324058532715 seconds

import math

sum = 0
value = str(math.factorial(100))
for i in range(0, len(value)):
    sum+=int(value[i])
print(sum)