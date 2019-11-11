# Tuple cannot be changed once declared
# tuple can be arguments passed into a function, and obtain several return values
# the '()' after the format strings are tuples
print('Method 1: %s is %d years old, and he is %.2f metres tall' % ('Leo', 18, 1.78))

# Method 2
info_tuple = ('Leo', 18, 1.78)
print('Method 2: %s is %d years old, and he is %.2f metres tall' % info_tuple)

# Method 3
info_str = 'Method 3: %s is %d years old, and he is %.2f metres tall' % info_tuple
print(info_str)

# can declare emtpy tuple, but this is not common
empty_tuple = ()

# ',' must be added to declare a tuple with one element
# otherwise it will just be the variable
solo_tuple = ('Leo',)

# 1. index - return the index of the first occurrence of a known value
print(info_tuple)
print(info_tuple[0])
print(info_tuple.index('Leo'))

# 2. count --- returns how many times an element has occurred
print(info_tuple.count('Leo'))

# Tuple can be converted into list, and vice versa
info_list = list(info_tuple)
print(type(info_list))

info_tuple2 = tuple(info_list)
print(type(info_tuple2))