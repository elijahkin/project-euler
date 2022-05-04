def concatenatedProduct(x, y):
    product = ''
    for i in range(1, y+1):
        product += str(x*i)
    return product

def isPandigital(x):
    if (1, 2, 3, 4, 5, 6, 7, 8, 9) in (int(i) for i in str(x)):
        return True
    else:
        return False

print(concatenatedProduct(9, 5))
print(isPandigital(123456789))