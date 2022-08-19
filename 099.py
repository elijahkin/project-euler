# 709
# Found answer in 0.04442119598388672 seconds

import math, csv

# Returns True if b2**e2 is greater than b1**e1
def exp_compare(b1, e1, b2, e2):
    return e1 < (math.log(b2, b1) * e2)

max_b = 2
max_e = 1
max_line_num = None

with open('data/099.csv', 'r') as file:
    reader = csv.reader(file)
    line_num = 0
    for pair in reader:
        line_num += 1
        cur_b = int(pair[0])
        cur_e = int(pair[1])
        if exp_compare(max_b, max_e, cur_b, cur_e):
            max_b = cur_b
            max_e = cur_e
            max_line_num = line_num

print(max_line_num)