class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "My name is %s, I'm %.2fkg" % (self.name, self.weight)

    def run(self):
        print("%s loves running" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s loves eating" % self.name)
        self.weight += 1


leo = Person("Leo", 62.0)
leo.run()
leo.eat()
print(leo)

jenny = Person("Jenny", 50.0)
jenny.eat()
jenny.run()
print(jenny)
