from ..enemy import Enemy, Intent
import random


class AcidSlime(Enemy):
    def __init__(self):
        super().__init__(random.randrange(65, 69))

    def corrosive_spit(self, is_acting=False):
        intent = Intent.AGGRESSIVE
        damage = 11

        # NEED TO ADD TWO SLIMED CARDS INTO THE DISCARD PILE
        # THESE GIVE THE CONDITION EXHAUSTED

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
