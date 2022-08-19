for i in range(1001, 10000):
    i = str(i)
    if i[1] != i[2]:
        continue
    numerator = int(i[:2])
    denominator = int(i[2:])
    numeratorShort = int(i[0])
    denominatorShort = int(i[3])
    if denominator == 0 or denominatorShort == 0:
        continue
    if (numerator/denominator) == (numeratorShort/denominatorShort):
        print(i)

print(1/((16/64)*(19/95)*(26/65)*(49/98)))