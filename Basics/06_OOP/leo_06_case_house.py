class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("Type: %s\nTotal area: %.2f[Free area: %.2f]\nFurniture: %s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("Adding...", item)
        # determine if the item fits in the house
        if item.area > self.free_area:
            print("%s is too large to fit" % item.name)
            return

        self.item_list.append(item.name)
        self.free_area -= item.area


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] uses %.2f" % (self.name, self.area)


bed = HouseItem("Bed A", 40)
chest = HouseItem("Chest A", 2)
table = HouseItem("Table A", 20)

print(bed)
print(chest)
print(table)

# Make House object
my_home = House("House", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
