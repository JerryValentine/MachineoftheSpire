from cards.card import Card, CardType
from units.player import Player
from units.enemies.enemy import Enemy


class Strike(Card):
    def __init__(self):
        super().__init__()
        self.type = CardType.ATTACK
        self.cost = 1
        self.dmg = 6

    def upgrade(self):
        self.dmg = 9

    def play(self, player: Player, target: Enemy):
        dmg = self.calculate_dmg(player, target)
        target.take_dmg(dmg)
