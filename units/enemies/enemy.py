from ..unit import Unit
from enum import Enum


class Intent(Enum):
    AGGRESSIVE = 1
    DEFENSIVE = 2
    STRATEGIC_DEBUFF = 3
    STRATEGIC_BUFF = 4
    AGGRESSIVE_DEBUFF = 5
    AGGRESSIVE_DEFENSE = 6
    AGGRESSIVE_Buff = 7
    DEFENSIVE_BUFF = 8
    COWARDLY = 9
    SLEEPING = 10
    STUNNED = 11
    UNKOWN = 12


class Enemy(Unit):
    def __init__(self, hp):
        super().__init__(hp)
        self.poison = 0
        self.shackled = 0
        self.slow = 0

    def take_dmg(self, dmg):
        if (self.vulnerable > 1):
            dmg = dmg * 1.5

        self.shield -= dmg
        if (self.shield < 0):
            self.hp += self.shield
            self.shield = 0
