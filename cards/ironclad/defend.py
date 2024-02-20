from cards.card import Card, CardType
from units.player import Player
from units.enemies.enemy import Enemy


class Defend(Card):
    def __init__(self):
        super().__init__()
        self.type = CardType.SKILL
        self.cost = 1
        self.block = 5

    def upgrade(self):
        self.block = 8

    # TODO: Don't love the idea of adding enemy as a parameter here, but it's a quick fix for now
    def play(self, player: Player, enemy: Enemy):
        player.shield += (self.block + player.dexterity)
