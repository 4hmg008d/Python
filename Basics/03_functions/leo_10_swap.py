a = 6
b = 100

# Method 1
c = a
a = b
b = c

# Method 2
a = a + b
b = a - b
a = a - b

# Method 3 - Python exclusive
# a, b = (b, a)
# RHS is also a tuple, () is omitted
a, b = b, a


print(a)
print(b)
