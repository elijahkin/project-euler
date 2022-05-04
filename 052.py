def isPermutedMultiple(x, multiplier):
    xDigits = [int(i) for i in str(x)]
    yDigits = [int(i) for i in str(x*multiplier)]
    for i in xDigits:
        if i not in yDigits:
            return False
    for i in yDigits:
        if i not in xDigits:
            return False
    return True

doubles = []
triples = []
quadruples = []
quintuples = []
sextuples = []

for i in range(1, 1000000):
    if isPermutedMultiple(i, 2) == True:
        doubles.append(i)

for i in doubles:
    if isPermutedMultiple(i, 3) == True:
        triples.append(i)

for i in triples:
    if isPermutedMultiple(i, 4) == True:
        quadruples.append(i)

for i in quadruples:
    if isPermutedMultiple(i, 5) == True:
        quintuples.append(i)

for i in quintuples:
    if isPermutedMultiple(i, 6) == True:
        sextuples.append(i)

print(sextuples)