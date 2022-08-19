# 5482660
# Found answer in 2.561389923095703 seconds

def is_pentagonal(P):
    n = (1+(1+24*P)**0.5)/6
    return (n % 1 == 0)

def pentagonal(n):
    P = n * (3*n-1) // 2
    return P

# Pretty brute-forcy, but it works!
k = 1
while True:
    for j in range(1, k):
        P_j, P_k = pentagonal(j), pentagonal(k)

        S = P_k + P_j
        D = P_k - P_j

        if is_pentagonal(D) and is_pentagonal(S):
            print(D)
            quit()
    k += 1