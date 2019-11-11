class Animal:

    def eat(self):
        print("Eat---")

    def drink(self):
        print("Drink---")

    def run(self):
        print("Run---")

    def sleep(self):
        print("Sleep---")


class Dog(Animal):
    # child class has all of parent class's attributes and methods
    # transitive property
    def bark(self):
        print("Wang Wang Wang")


class XiaoTianQuan(Dog):

    def fly(self):
        print("I can fly")

    # child class can overwrite parent's methods
    # use the same function name as parent class's function
    def bark(self):
        # function specific for child class
        print("I can speak English")
        # use super(). to include methods from parent class
        super().bark()
        # Other child function
        print("$%^$%^$%^*$%^*$")


class Cat(Animal):
    def catch(self):
        print("Catch mouse")


elsa = XiaoTianQuan()
elsa.eat()
elsa.drink()
elsa.run()
elsa.sleep()
elsa.bark()
elsa.fly()
# elsa cannot use methods or attributes in Cat class
# elsa.catch()
