# 31875000
# Found answer in 0.041932106018066406 seconds

# a^2+b^2=c^2 and a+b+c=1000 --> b=(1000^2-2000a)/(2000-2a)
for a in range(1000):
    b = (1000*1000-2000*a) // (2000-2*a)
    c = 1000 - a - b
    if a > 0 and b > 0 and c > 0:
        if a*a+b*b == c*c:
            break
print(a*b*c)