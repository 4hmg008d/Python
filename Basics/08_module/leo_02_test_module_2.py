def say_hello():
    print("I'm module 2")


class Cat:
    pass


# if run inside this file --> output __main__, if imported --> output file name
if __name__ == "__main__":
    print(__name__)
    print("Leo designed module")
    say_hello()