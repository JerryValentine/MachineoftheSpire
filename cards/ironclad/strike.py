from cards.card import Card
from units.player import Player
from units.enemies.enemy import Enemy


class Strike(Card):
    def __init__(self):
        super().__init__()
        self.cost = 1
        self.dmg = 6

    def play(self, player: Player, target: Enemy):
        dmg = self.calculate_dmg(player, target)
        target.take_dmg(dmg)
