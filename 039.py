counts = []

for p in range(1, 1001):
    count = 0
    for a in range(1, int(p/2)):
        for b in range(1, a+1):
            if a + b + (a**2+b**2)**0.5 == p:
                count+=1
            else:
                continue
    counts.append(count)

print(counts.index(max(counts))+1)