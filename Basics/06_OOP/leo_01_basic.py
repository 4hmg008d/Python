# Create Cat class
class Cat:

    def eat(self):
        # self is the reference to the object whose method has been called
        print("%s likes eating fish" % self.name)

    def drink(self):
        print("%s likes drinking water" % self.name)


# Create cat object
tom = Cat()
# Add attributes externally, easy but not recommended
tom.name = "Tom"
tom.eat()
tom.drink()

print(tom)


# Another cat object
lazy_cat = Cat()
lazy_cat.name = "Krystal"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)

addr = id(tom)
print("%x" % addr)