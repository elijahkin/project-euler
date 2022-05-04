def lattice_paths(n):

    # Set up matrix
    paths = [[0 for c in range(n+1)] for r in range(n+1)]

    # Iterate through and fill in values
    for x in range(0, n+1):
        for y in range(0, n+1):
            v = 0
            if x == 0 and y == 0:
                v = 1
            if x != 0:
                v += paths[x-1][y]
            if y != 0:
                v += paths[x][y-1]
            paths[x][y] = v

    return paths[n][n]

print(lattice_paths(20))