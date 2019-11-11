def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


def sum_numbers(*args):
    num = 0

    for n in args:
        num+=n
    return num


demo(1)
demo(1, 2, 3, 4, 5, name="Leo", age=16)

gl_nums = (1,2,3)
gl_leo = {"name":"Leo", "age":16}

result = sum_numbers(1,2,3,4,5)
print(result)

demo(0, *gl_nums, ** gl_leo)