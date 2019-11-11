# __str__ must return strings
class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        # called before removing the object
        print("%s is leaving" % self.name)

    def __str__(self):
        # used to return string instead of <object type> + <address>
        # must return a string
        return "I'm cat [%s]" % self.name


# Tom is a global variable
tom = Cat("Tom")
print(tom)