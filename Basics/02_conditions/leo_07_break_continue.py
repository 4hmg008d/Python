# Break -- stop at 2
i = 0

while i < 5:

    print(i)

    if i == 2:
        break

    i += 1

print('over')

# Continue -- skip 2
i = 0

while i < 5:

    print(i)

    # Be careful: change counter before 'continue', otherwise infinite loop
    if i == 2:
        i += 1
        continue

    i += 1

print('over')