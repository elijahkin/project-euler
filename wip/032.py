def isPandigital(n):
    n = [int(i) for i in str(n)]
    for i in range(1, len(n)+1):
        if i not in n:
            return False
    return True

print(isPandigital(15234))