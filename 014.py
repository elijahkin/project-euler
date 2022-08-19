# 837799
# Found answer in 24.736983060836792 seconds

def collatz(x):
    iterations = 1
    while x != 1:
        if x % 2 == 0 and x != 0:
            x = x / 2
        else:
            x = 3*x + 1
        iterations += 1
    return iterations

chains = []
for i in range(0, 1000001):
    chains.append(collatz(i))
print(chains.index(max(chains)))