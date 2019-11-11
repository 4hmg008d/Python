class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 1. __new__ is always called when creating new object
        print("creating object, allocating memory...")

        # 2. allocating memory
        location = super().__new__(cls)

        # 3. return object's reference, this is then passed to __init__
        return location

    def __init__(self):
        print("Initialising player...")


player = MusicPlayer()

print(player)
