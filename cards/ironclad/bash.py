from cards.card import Card, CardType
from units.player import Player
from units.enemies.enemy import Enemy


class Bash(Card):
    def __init__(self):
        super().__init__()
        self.type = CardType.ATTACK
        self.cost = 2
        self.dmg = 8
        self.vulnerable = 2

    def upgrade(self):
        self.dmg = 10
        self.vulnerable = 3

    def play(self, player: Player, target: Enemy):
        dmg = self.calculate_dmg(player, target)
        target.take_dmg(dmg)
        target.vulnerable += self.vulnerable
