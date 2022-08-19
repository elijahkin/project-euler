# 1366
# Found answer in 0.04411888122558594 seconds

def exponentiateString(x, y):
    return sum(list(map(int, str(x**y))))

print(exponentiateString(2, 1000))