def convergent(x, y, z):
    convergent = 0
    for i in range(1, z):
        convergent += y[-i]
        convergent = 1 / convergent
    convergent += x
    print(convergent)
    for i in range(1, 100000000000):
        if (convergent * i) % 1 == 0:
            return int(convergent * i)

def sequence():
    sequence = []
    for i in range(1, 34):
        sequence.append(1)
        sequence.append(2*i)
        sequence.append(1)
    return sequence

print(convergent(2, sequence(), 100))

sum = 0
numerator = str(convergent(2, sequence(), 100))
for i in numerator:
    sum += int(i)
print(sum)