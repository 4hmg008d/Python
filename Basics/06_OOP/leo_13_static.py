class Dog(object):

    @staticmethod
    def run():
        # no using object method / attribute
        print("Dog is running")


# No need to create object
Dog.run()
