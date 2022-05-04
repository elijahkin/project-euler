distinctPowers = []

max = 101

for a in range(2, max):
    for b in range(2, max):
        power = a**b
        if power not in distinctPowers:
            distinctPowers.append(power)
print(len(distinctPowers))