# dictionary is unordered, print order may be different as defined
info = {'name': 'Leo',
        'age': 18,
        'gender': True,
        'height': 1.78,
        'weight': 60}

print(info)

print(len(info))

tmp = {'size': 9,
       'colour': 'yellow',
       'height': 2.00}

# 1. Obtain value by entering key
print(info['name'])  # error if key does not exist
print(info.get('asdofiajrgin'))  # no error if key does not exist
print(info.keys())
print(info.values())
print(info.items())

# 2. Change values
info['age'] = 21
info.setdefault('age', 18)  # if key exists, nothing will happen; if not, new key will be added

# 3. Adding values
# Key will be added if no key exists
info['nickname'] = 'Liejin'
print(info)

info.update(tmp)
print(info)

# 4. Remove
info.pop('nickname')
print(info)

print(info.popitem())  # popped item could be random
print(info)
info.clear()

# For loop
for k in tmp:
    print('%s - %s' % (k, tmp[k]))

# For loop case
card_list = [
    {'name': 'Leo',
     'QQ': 12345,
     'Phone': 1634645},
    {'name': 'Sam',
     'QQ': 1235673,
     'Phone': 24356},
]

for card_info in card_list:
    print(card_info['name'])
