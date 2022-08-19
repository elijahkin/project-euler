# 49
# Found answer in 0.04512786865234375 seconds

n = 1
count = 0

while True:
    this_n_count = 0
    for b in range(0, 10):
        # Only have to check this b^n will always be less than 10^n since b ranges [0, 9]
        if b**n >= 10**(n-1):
            this_n_count += 1
    # Know to end once there comes an n that gives you none (monotonically decreasing)
    if this_n_count == 0:
        break
    else:
        count += this_n_count
        n += 1

print(count)