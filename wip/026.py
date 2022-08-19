#Solved without a program - Answer is 983

import numpy as np
from decimal import *

def reciprocalCycle(x):
    cycle = str(1 / Decimal(x))[2:]
    cyclePeriod = cycle.find(cycle[0], 1)
    return cyclePeriod

getcontext().prec = 500
cycles = []
for i in range(2, 1001):
    cycles.append(reciprocalCycle(i))
print(cycles.index(max(cycles))+2)