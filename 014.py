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
print("Chain of", max(chains), "at i=", chains.index(max(chains)))