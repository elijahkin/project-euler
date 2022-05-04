def generate_pandigitals(available_digits):
    if available_digits == []:
        return []
    else:
        pandigitals = []
        for i in available_digits:
            new_digits = list(available_digits)
            new_digits.remove(i)

            rec = generate_pandigitals(new_digits)
            for n in rec:
                pandigitals.append([i]+n)

        return pandigitals

print(generate_pandigitals([0, 1, 2, 3]))

# def isPandigital(x):
#     x = [int(i) for i in str(x)]
#     for i in range(10):
#         if i not in x:
#             return False
#     return True

# pandigitals = []
# for i in range(1023456789, 9876543211):
#     if isPandigital(i) == True:
#         pandigitals.append(i)
# print(pandigitals)

