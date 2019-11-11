def sum_2_sum(num1, num2):
    result = num1 + num2

    print('%d + %d = %d' % (num1, num2, result))


def sum_return(num1, num2):
    return num1 + num2


sum_2_sum(1, 2)
result = sum_return(3, 4)
print('The result is: %d' % result)
