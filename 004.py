palindromes = []
for multiplier1 in range(100, 1000):
    for multiplier2 in range(100, 1000):
        product = str(multiplier1*multiplier2)
        if product[0]==product[-1]:
            if product[1]==product[-2]:
                if product[2]==product[-3]:
                    palindromes.append(int(product))
print(max(palindromes))