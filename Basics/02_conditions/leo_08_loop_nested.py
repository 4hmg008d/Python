i = 0

while i < 6:
    print("*" * i)
    i += 1

# print can have different endings
print("*", end="---")
print("*")

# Method two
i = 0
j = 0

while i < 6:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1

# 9 * 9 table
i = 1
j = 1

while i <= 9:
    j = 1
    while j <= i:
        # Use \t to align vertically
        print("%d x %d = %d" % (j, i, j * i), end="\t")
        j += 1
    print("")
    i += 1

