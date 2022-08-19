# 233168
# Found answer in 0.04070091247558594 seconds

# Returns sum of all multiples of m less than n
def sum_multiples_up_to(m, n):
    k = (n - 1) // m
    return m * (k * (k+1)) // 2

n = 1000
# Inclusion-exclusion principle
sum = sum_multiples_up_to(3, n) + sum_multiples_up_to(5, n) - sum_multiples_up_to(15, n)
print(sum)