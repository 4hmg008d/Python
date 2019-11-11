class A:
    def test(self):
        print("test method --- A")

    def domo(self):
        print("demo method --- A")


class B:
    def test(self):
        print("test method --- B")

    def domo(self):
        print("demo method --- B")


# parent classes should not have the same attributes or methods
class C(A, B):
    pass


c = C()
c.test()
c.domo()

# determine C's method resolution order (MRO)
print(C.__mro__)