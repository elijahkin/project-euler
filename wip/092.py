# def sum_of_squared_digits(n):
#     sum = 0
#     for d in str(n):
#         sum += int(d)**2
#     return sum

# successor_lookup = dict()
# for i in range(10000000):
#     successor_lookup[i] = sum_of_squared_digits(i)

# def chain_starting_at(seed):
#     chain = [seed]
#     while True:
#         successor = successor_lookup[chain[-1]]
#         if successor in chain:
#             break
#         else:
#             chain.append(successor)
#     for i in chain:
#         successor_lookup[i] = successor

# print(successor_lookup)

# BROKEN

def digitize(n):
    return [int(d) for d in str(n)]

def sum_of_squares(list):
    sum = 0
    for i in list:
        sum += i**2
    return sum

terminus = dict()
terminus[1] = 1
terminus[89] = 89

# rework
for i in range(1, 100):
    print(i)
    terminus[i] = terminus[sum_of_squares(digitize(i))]
print(terminus)