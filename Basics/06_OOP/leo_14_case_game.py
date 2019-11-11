class Game(object):
    # history highest score
    top_score = 0

    def __init__(self, player):
        self.player_name = player

    @staticmethod
    def show_help():
        print("Top: let zombies through!")

    @classmethod
    def show_top_score(cls):
        print("Highest: %d" % cls.top_score)

    def start_game(self):
        print("%s starts playing" % self.player_name)


# 1. show help
Game.show_help()

# 2. show top score
Game.show_top_score()

# 3. create player object
game = Game("Leo")
game.start_game()