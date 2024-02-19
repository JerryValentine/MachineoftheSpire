from unit import Unit
from enemy import Enemy
import random


class JawWorm(Enemy):
    def __init__(self):
        super().__init__(random.randrange(40, 45))
        self.block = 0
        self.strength = 0

    def chomp(self, target: Unit):
        target.hp -= 11

    def thrash(self, target: Unit):
        self.block += 5
        target.hp -= 7

    def bellow(self):
        self.strength += 3
        self.sheild += 6

    def act(self, round, target: Unit):
        action_chance = random.randrange(100)

        if (round == 1):
            self.chomp(target)
        else:
            if (action_chance < 45):
                self.bellow()
            elif (action_chance < 75):
                self.thrash(target)
            else:
                self.chomp(target)
