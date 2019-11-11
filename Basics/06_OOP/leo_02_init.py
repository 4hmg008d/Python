class Cat:

    def __init__(self, new_name):
        # used to declare initial / default attributes
        print("Initialising ......")

        self.name = new_name


    def eat(self):
        print("%s likes eating fish" % self.name)


tom = Cat("Tom")
lazy_cat = Cat("Krystal")

print(tom.name)

lazy_cat.eat()
