fibonacci = [1,1,1]
evenFibonnaci = []
counter = 0
while counter < 4000000:
    counter = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(counter)
for nums in fibonacci:
    if nums % 2 == 0:
        evenFibonnaci.append(nums)
print(sum(evenFibonnaci))

# New Techniques:
# using string[-1] to get the last character

# f = [1, 2]
# s = 0
# while f[-1] < 2472136:
#     f.append(f[-1] + f[-2])
# for i in f:
#     if i % 2 == 0:
#         s += i
# print(s)