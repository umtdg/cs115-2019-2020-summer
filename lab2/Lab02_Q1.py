# a:
sum1 = 1
for i in range(2, 1001):
    sum1 += 1/i

# one liner:
# sum1 = sum([1/x for x in range(1, 1001)])

# b:
sum2 = 1
i = 2
while i < 1001:
    sum2 += 1/i
    i += 1

print("Sum with for: {}\nSum with while: {}".format(
    sum1,
    sum2
))
