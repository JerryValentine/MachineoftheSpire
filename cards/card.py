from units.player import Player
from units.enemies.enemy import Enemy


class Card():
    def __init__(self):
        self.cost = 0
        self.dmg = 0
        self.block = 0

    def calculate_dmg(self, player: Player, target: Enemy):
        dmg = self.dmg + player.strength
        if (player.weakened > 0):
            dmg = dmg * 0.75

        return dmg

    def play(self, player, target):
        print("card not implemented yet")
        pass
