from units.player import Player
from units.enemies.enemy import Enemy
from enum import Enum


class CardType(Enum):
    ATTACK = 1
    SKILL = 2
    POWER = 3
    STATUS = 4
    CURSE = 5


class Card():
    def __init__(self):
        self.type = None
        self.cost = 0
        self.dmg = 0
        self.block = 0

    def exhaust(self, player: Player):
        player.exhaust.append(self)
        player.hand.remove(self)

    def calculate_dmg(self, player: Player, target: Enemy):
        dmg = self.dmg + player.strength
        if (player.weakened > 0):
            dmg = dmg * 0.75

        return dmg

    def upgrade(self):
        print("card not implemented yet")
        pass

    def play(self, player, target):
        print("card not implemented yet")
        pass
