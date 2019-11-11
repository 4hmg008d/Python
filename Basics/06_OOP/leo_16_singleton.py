class MusicPlayer(object):

    # record address for the first object
    instance = None

    # record if __init__ has been called
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. determine if class attribute is none
        if cls.instance is None:
            # 2. allocate memory for the first object
            cls.instance = super().__new__(cls)

        # return the memory address
        return cls.instance

    def __init__(self):
        # 1. determine if initialisation has been done
        if MusicPlayer.init_flag:
            return

        # 2. if not initialised yet...
        print("Initialising")

        # 3. change init.flag
        MusicPlayer.init_flag = True


# create multiple objects
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
