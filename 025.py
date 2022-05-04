fibonacci = [1, 1]

while max(fibonacci) < 10**999:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(len(fibonacci))