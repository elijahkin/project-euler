# 210
# Found answer in 0.156937837600708 seconds

fractionalPart = ''
i=1
while len(fractionalPart) < 1000000:
    fractionalPart += str(i)
    i+=1
print(int(fractionalPart[0])*int(fractionalPart[9])*int(fractionalPart[99])*int(fractionalPart[999])*int(fractionalPart[9999])*int(fractionalPart[99999])*int(fractionalPart[999999]))