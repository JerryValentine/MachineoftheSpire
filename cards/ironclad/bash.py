from cards.card import Card, CardType
from units.unit import Unit


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

    def play(self, **units: Unit):
        dmg = self.calculate_dmg(units['player'], units['target'])
        units['target'].take_dmg(dmg)
        units['target'].vulnerable += self.vulnerable
