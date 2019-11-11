def print_line(char, times):
    """
    Print separator line
    :param char: type of separator
    :param times: repeated times per line
    """
    print(char * times)


def print_lines(char, times):
    """
    Print multiple separator lines
    :param char: type of separator
    :param times: repeated times per line
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines('+', 20)