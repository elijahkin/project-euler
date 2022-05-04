import csv

longs = []

with open('Euler13.csv', mode='r', newline='') as data:
    dataReader = csv.reader(data, delimiter=',')
    for row in dataReader:
        longs.append(int(row[0]) / (10**40))

print(sum(longs))