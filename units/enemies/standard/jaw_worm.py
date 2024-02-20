from ..enemy import Enemy, Intent
import random


class JawWorm(Enemy):
    def __init__(self):
        super().__init__(random.randrange(40, 45))

    def chomp(self, is_acting=False):
        intent = Intent.AGGRESSIVE
        damage = 11 + self.strength

        return (intent, damage)

    def thrash(self, is_acting=False):
        intent = Intent.AGGRESSIVE_DEFENSE
        damage = 7 + self.strength

        if (is_acting):
            self.sheild += 5

        return (intent, damage)

    def bellow(self, is_acting=False):
        intent = Intent.DEFENSIVE_BUFF
        damage = 0

        if (is_acting):
            self.strength += 3
            self.sheild += 6

        return (intent, damage)

    def get_action(self, round, action_chance=None):
        if action_chance is None:
            action_chance = random.randrange(0, 100)

        if (round == 1):
            return self.chomp
        else:
            if (action_chance < 45):
                return self.bellow
            elif (action_chance < 75):
                return self.thrash
            else:
                return self.chomp
