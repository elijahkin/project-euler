def exponentiateString(x, y):
    return sum(list(map(int, str(x**y))))

print(exponentiateString(2, 1000))