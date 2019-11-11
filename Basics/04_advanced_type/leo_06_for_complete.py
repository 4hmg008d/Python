for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # if exited by break, 'else' will not be reached
    print('Reached "else"!')

print('Finished!')

students = [
    {'name': 'Leo'},
    {'name': 'Krystal'}
]

find_name = 'Sam'
for people in students:
    print(people)
    if people['name'] == find_name:
        print('Found %s' % find_name)
        break
else:
    # this will be executed after all loops have been done
    print('Not found %s' % find_name)
