# Brute force (SLOW)
# sum = 0
# for i in range(1000):
#     if (i % 3 == 0) or (i % 5 == 0):
#         sum += i
# print(sum)

# Returns sum of all multiples of m less than n
def sum_multiples_up_to(m, n):
    k = (n - 1) // m
    return m * (k * (k+1)) // 2

n = 1000
# Inclusion-exclusion principle
sum = sum_multiples_up_to(3, n) + sum_multiples_up_to(5, n) - sum_multiples_up_to(15, n)
print(sum)