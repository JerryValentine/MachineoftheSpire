from ..enemy import Enemy, Intent
from cards.neutral.slimed import Slimed
from units.unit import Unit
import random


class AcidSlimeLarge(Enemy):
    def __init__(self):
        super().__init__(random.randrange(65, 69))
        self.starting_hp = self.hp

    def corrosive_spit(self, **units: Unit):
        intent = Intent.AGGRESSIVE_DEBUFF
        damage = 11
        units['player'].add_to_discard([Slimed(), Slimed()])
        return (intent, damage)

    def lick(self, **units: Unit):
        intent = Intent.DEBUFF
        damage = 0
        units['player'].weakened += 2
        return (intent, damage)

    def tackle(self):
        intent = Intent.AGGRESSIVE
        damage = 16
        return (intent, damage)

    def split(self):
        self.hp = 0
        intent = Intent.Unknown
        return (intent, [AcidSlimeMedium(), AcidSlimeMedium()])

    def get_action(self, round, action_chance=None):
        if action_chance is None:
            action_chance = random.randrange(0, 100)

        if (self.hp <= .5 * self.starting_hp):
            return self.split
        elif (action_chance < 30):
            return self.corrosive_spit
        elif (action_chance < 70):
            return self.tackle
        else:
            return self.lick


class AcidSlimeMedium(Enemy):
    def __init__(self):
        super().__init__(random.randrange(28, 32))
        self.starting_hp = self.hp

    def corrosive_spit(self, **units: Unit):
        intent = Intent.AGGRESSIVE_DEBUFF
        damage = 7
        units['player'].add_to_discard([Slimed()])
        return (intent, damage)

    def lick(self, **units: Unit):
        intent = Intent.DEBUFF
        damage = 0
        units['player'].weakened += 1
        return (intent, damage)

    def tackle(self):
        intent = Intent.AGGRESSIVE
        damage = 10
        return (intent, damage)

    def get_action(self, round, action_chance=None):
        if action_chance is None:
            action_chance = random.randrange(0, 100)

        if (action_chance < 30):
            return self.corrosive_spit
        elif (action_chance < 70):
            return self.tackle
        else:
            return self.lick


class AcidSlimeSmall(Enemy):
    def __init__(self):
        super().__init__(random.randrange(8, 12))
        self.starting_hp = self.hp
        self.alternate_move = False

    def lick(self, **units: Unit):
        intent = Intent.DEBUFF
        damage = 0
        units['player'].weakened += 1
        return (intent, damage)

    def tackle(self):
        intent = Intent.AGGRESSIVE
        damage = 3
        return (intent, damage)

    def get_action(self, round, action_chance=None):
        if action_chance is None:
            action_chance = random.randrange(0, 100)

        if (round == 1):
            if (action_chance < 50):
                self.alternate_move = True
                return self.lick
            else:
                self.alternate_move = False
                return self.lick
        elif (self.alternate_move is False):
            self.alternate_move = True
            return self.tackle
        else:
            self.alternate_move = False
            return self.lick
