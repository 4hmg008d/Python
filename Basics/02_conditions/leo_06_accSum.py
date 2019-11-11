i = 0
total = 0
while i <= 100:
    total += i
    i += 1
print('The sum is %d' % total)

total = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print('The sum of all even number is %d' % total)
