# 249
# Found answer in 0.1804201602935791 seconds

def flip(n):
    return int(str(n)[::-1])

def isPalidrome(n):
    n = [int(i) for i in str(n)]
    for i in range(0, len(n)):
        if n[i] != n[-i-1]:
            return False
    return True

def isLychrel(n):
    for i in range(1, 51):
        n += flip(n)
        if isPalidrome(n) == True:
            return False
    return True

lychrels = []
for i in range(10001):
    if isLychrel(i) == True:
        lychrels.append(i)
print(len(lychrels))