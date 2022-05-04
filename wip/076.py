def count_sums(x):
    count = 1
    for i in range(x, 0, -1):
        print(str(i) + ": " + str(count))

count_sums(5)