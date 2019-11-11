class Soldier:
    def __init__(self, name):
        self.name = name

        # if no initial value, we can use None
        # "None" can use all methods from all classes!!
        self.gun = None

    def fire(self):
        # 1. determine if the soldier has a gun
        # 'is' checks if 2 objects are pointing to the same memory
        # '==' checks if 2 values are equal
        if self.gun is None:
            print("[%s] does not have a gun yet..." % self.name)
            return

        # 2. Yayayaaaaaaaaaah
        print("Yaaaaaaaaaaah [%s]" % self.name)

        # 3. Loading
        self.gun.add_bullet(50)

        # 4. Shoot
        self.gun.shoot()


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s] has no bullets..." % self.model)
            return

        self.bullet_count -= 1
        print("[%s] Da da da ... [%d]" % (self.model, self.bullet_count))


# 1. create gun object
ak47 = Gun("AK-47")

# 2. create soldier object
sam = Soldier("Sam")
sam.gun = ak47
sam.fire()
