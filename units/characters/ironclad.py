import random
from ..player import Player
from cards.ironclad.strike import Strike
from cards.ironclad.defend import Defend
from cards.ironclad.bash import Bash


class Ironclad(Player):
    def __init__(self, hp: int):
        super().__init__(hp)
        self.deck = self._generate_starting_deck()

    def _generate_starting_deck(self):
        deck = [Strike() for _ in range(5)]
        deck += [Defend() for _ in range(4)]
        deck.append(Bash())
        random.shuffle(deck)

        return deck
