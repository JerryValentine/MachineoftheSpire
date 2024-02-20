from ..card import Card
from ...units.player import Player
from ...units.enemies.enemy import Enemy


class strike(Card):
    def __init__(self):
        super().__init__()
        self.cost = 1
        self.attack = 6

    def play(self, player: Player, target: Enemy):
        dmg = self.attack + player.strength
        if (player.weakened > 0):
            dmg = dmg * 0.75
