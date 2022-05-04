def rect(x, y):
    return int(x*(x+1)*y*(y+1)/4)

r = 2000000
a = None
for x in range(100):
    for y in range(100):
        if abs(2000000-rect(x, y)) < r:
            r = abs(2000000-rect(x, y))
            a = x*y
print(a)

"""
I first worked a few small examples by hand, and noticed that whenever
x==1, the result was a triangle number: (1, 1+2, 1+2+3, 1+2+3+4...) = (1, 3, 6, 10...)

f(1, 1) = 1
f(1, 2) = 3
f(1, 3) = 6
f(1, 4) = 10
f(2, 2) = 9
f(2, 3) = 18

With this information, I wrote the following:

def rect(x, y):
    return tri(x)*tri(y)

def tri(n):
    return int(n*(n+1)/2)

And later simplified the code into the algorithm I use now
"""