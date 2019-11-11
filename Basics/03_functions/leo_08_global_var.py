# global variable
# declared on top of all functions
gl_num = 10


def demo1():
    # use 'global' to change global variable, otherwise it will create a new var
    global gl_num
    gl_num = 99

    print("demo1 ==> %d" % gl_num)


def demo2():

    print("demo1 ==> %d" % gl_num)


demo1()
demo2()
