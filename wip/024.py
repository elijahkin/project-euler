# BROKEN

import math

def nth_permutation(digits, n):

    string = ''
    while len(digits) > 0:
        i = n // math.factorial(len(digits)-1)

        string += str(digits[i])
        digits.pop(i)

        n -= math.factorial(len(digits)) * i
    return string

print(nth_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10**6+1))

# for _ in range(math.factorial(4)):
#     print(nth_permutation([0, 1, 2, 3], _))

# VERIFICATION
# import itertools
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def nthPermutation(x, y):
#     return list(itertools.permutations(x))[y]
# print(nthPermutation(digits, 1000000))