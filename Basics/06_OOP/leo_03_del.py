class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        # called before removing the object
        print("%s is leaving" % self.name)


# Tom is a global variable
tom = Cat("Tom")
print(tom.name)

# del is used to remove an object
del tom

print("-" * 50)
