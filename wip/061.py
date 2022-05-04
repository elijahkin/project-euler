triangle = [0]
n = 0
while triangle[-1] < 10000:
    triangle.append(int(n*(n+1)/2))
    n += 1

square = [0]
n = 0
while square[-1] < 10000:
    square.append(n**2)
    n += 1

pentagonal = [0]
n = 0
while pentagonal[-1] < 10000:
    pentagonal.append(int(n*(3*n-1)/2))
    n += 1

hexagonal = [0]
n = 0
while hexagonal[-1] < 10000:
    hexagonal.append(int(n*(2*n-1)))
    n += 1

heptagonal = [0]
n = 0
while heptagonal[-1] < 10000:
    heptagonal.append(int(n*(5*n-3)/2))
    n += 1

octagonal = [0]
n = 0
while octagonal[-1] < 10000:
    octagonal.append(int(n*(3*n-2)))
    n += 1

print(triangle)
print(square)
print(pentagonal)
print(hexagonal)
print(heptagonal)
print(octagonal)