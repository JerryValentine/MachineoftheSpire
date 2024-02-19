class Unit:
    def __init__(self, hp):
        self.hp = hp
        self.sheild = 0
        self.stength = 0
        self.weakened = 0
        self.vulnerable = 0

    def is_alive(self):
        return self.hp > 0

    def act(self, target):
        print("TODO")

    def endstep(self):
        print("TODO")

    def __str__(self):
        return "{} has {} hit points.".format(self.name, self.hp)
