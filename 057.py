# 153
# Found answer in 0.0450589656829834 seconds

numerators = [3]
denominators = [2]
n = 1
d = 2

for i in range(1001):
    n += 2*d
    n,d = d,n
    denominators.append(d)
    numerators.append(n + d)

longerNumerators = 0
for i in range(0, len(numerators)):
    if len(str(numerators[i])) > len(str(denominators[i])):
        longerNumerators += 1

print(longerNumerators)