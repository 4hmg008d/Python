class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # non-public can be accessed internally
        print("%s is %d years old" % (self.name, self.__age))


krystal = Women("Krystal")

# non-public attributes cannot be accessed externally
# print(krystal.__age)
# Python added a special prefix to them: _object._class__variable
print(krystal._Women__age)

# non-public methods cannot be accessed externally
# krystal.__secret()
krystal._Women__secret()