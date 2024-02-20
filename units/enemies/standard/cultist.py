from ..enemy import Enemy, Intent
import random


class Cultist(Enemy):
    def __init__(self):
        super().__init__(random.randrange(48, 54))
        self.ritual = 0
        self.strength = 0

    def incantation(self, is_acting=False):
        intent = Intent.STRATEGIC_BUFF
        damage = 0

        if (is_acting):
            self.ritual += 3

        return (intent, damage)

    def dark_strike(self, is_acting=False):
        intent = Intent.AGGRESSIVE
        damage = (6 + self.strength)

        return (intent, damage)

    def act(self, round):
        if (round == 1):
            self.incantation
        else:
            self.dark_strike

    def endstep(self):
        super().endstep()
        self.strength += self.ritual
