def multiple_table():
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
