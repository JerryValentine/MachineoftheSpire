class Unit:
    def __init__(self, hp):
        self.hp = hp
        self.shield = 0
        self.strength = 0
        self.weakened = 0
        self.vulnerable = 0

    def is_alive(self):
        return self.hp > 0

    def get_action(self):
        print("TODO")

    def endstep(self):
        print("TODO")

    def __str__(self):
        return "{} has {} hit points.".format(self.__class__.__name__, self.hp)
