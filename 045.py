triangulars = []
pentagonals = []
hexagonals = []

for i in range(1, 100000):
    triangulars.append(int(i*(i+1)/2))
    pentagonals.append(int(i*(3*i-1)/2))
    hexagonals.append(int(i*(2*i-1)))

for i in triangulars:
    if i in pentagonals and i in hexagonals:
        print(i)