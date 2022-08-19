# 5537376230 39.0876?
# Found answer in 0.04597115516662598 seconds

import csv

longs = []

with open('data/013.csv', mode='r', newline='') as data:
    dataReader = csv.reader(data, delimiter=',')
    for row in dataReader:
        longs.append(int(row[0]) / (10**40))

print(sum(longs))