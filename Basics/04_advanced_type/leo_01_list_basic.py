name_list = ['Leo', 'Krystal', 'Mancai']

# 1. Index
print(name_list[2] + ' is at position %d' % (name_list.index(name_list[2]) + 1))

# 2. modify
name_list[2] = 'Keying'

# 3. Append, insert, extend
name_list.append('David')
name_list.insert(1, 'Liejin')

temp_list = ['Sam', 'Cameron', 'Ben']
# extend will add elements, "+=" is the same as extend, but 'list = list + list' is not the same
# whereas append will treat that as one 'list' element
name_list.extend(temp_list)
name_list += temp_list
name_list.append(temp_list)
print(name_list)
name_list.pop()

# 4. Len, count
print('The list has %d elements.' % len(name_list))
print('"Leo" has occurred %d times.' % name_list.count('Leo'))

# 5. Sort, reverse -- operation will change the list, but not return any value
print(name_list)

name_list.reverse()
print(name_list)

name_list.sort()
print(name_list)

name_list.sort(reverse=True)
print(name_list)

# 6. Remove, pop, clear and del
name_list.remove('Sam')
del name_list[2]
name_list.pop(3)
name_list.pop()
name_list.clear()

print(name_list)
