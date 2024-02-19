from ...unit import Unit
from ..enemy import Enemy
import random


class Cultist(Enemy):
    def __init__(self):
        super().__init__(random.randrange(48, 54))
        self.ritual = 0
        self.strength = 0

    def incantation(self):
        self.ritual += 3

    def dark_strike(self, target: Unit):
        target.hp -= (6 + self.strength)

    def act(self, round, target: Unit):
        if (round == 1):
            self.incantation()
        else:
            self.strength += self.ritual  # from ritual
            self.dark_strike(target)
