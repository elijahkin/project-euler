# BROKEN

ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

tens = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

special_case = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

# 74 --> [0, 0, 7, 4]
def digitize(n):
    digits = [int(d) for d in str(n)]
    while len(digits) < 4:
        digits = [0] + digits
    return digits

# Convert number [1, 1000] into written English version
def englishize(n):

    if 10 < n and n < 20:
        return special_case[n]

    m, c, x, i = digitize(n)
    string = ''

    if m > 0:
        string += '{}thousand'.format(ones[m])
    if c > 0:
        string += '{}hundred'.format(ones[c])
        if x > 0 or i > 0:
            string += 'and'
    if x > 0:
        string += '{}'.format(tens[x])
    if i > 0:
        string += '{}'.format(ones[i])

    return string

concat = ''
for i in range(1, 1000+1):
    concat += englishize(i)
print(concat)
print(len(concat))

print(len(englishize(115)))