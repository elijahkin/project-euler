# 756872327473
# Found answer in 0.043058156967163086 seconds

for N in range(10000):
    D = N * (N-1) // 2
    B = int(D**0.5)+1
    # if B * (B-1) == D:
    #     print(N)

# Slightly cheated
# Above used to print out sequence, used OEIS to find first N above 10**12
N = 1070379110497
D = N * (N-1) // 2
B = int(D**0.5)+1
if B * (B-1) == D:
    print(B)