import random
from copy import deepcopy as copy
from units.unit import Unit


class Player(Unit):
    def __init__(self, hp):
        super().__init__(hp)
        self.deck = []
        self.hand = []
        self.discard = []
        self.exhaust = []
        self.draw = 5
        self.confused = False
        self.dexterity = 0
        self.dexterity_down = 0
        self.stength_down = 0
        self.frail = 0
        self.no_draw = False
        self.constricted = 0
        self.draw_reduction = 0
        self.entangled = False
        self.hex = False
        self.no_block = 0

    def _generate_starting_deck(self):
        print("deck not implemented yet")
        pass

    def add_to_discard(self, cards: list):
        self.discard.extend(cards)

    def add_to_exhaust(self, cards: list):
        self.exhaust.extend(cards)

    def add_to_hand(self, cards: list):
        self.hand.extend(cards)

    def add_to_deck(self, cards: list):
        self.deck.extend(cards)

    def draw_hand(self):
        if len(self.deck) < self.draw:
            self.hand = self.deck[:self.draw - len(self.deck)]
            self.deck = copy(self.discard)
            self.discard = []
            random.shuffle(self.deck)
            self.hand += self.deck[:self.draw - len(self.hand)]
        else:
            self.hand = self.deck[:self.draw]
            self.deck = self.deck[self.draw:]

    def play_card(self, card, target):
        card.play(player=self, target=target)
        self.hand.remove(card)
        self.discard.append(card)

    def print_deck(self):
        for i, card in enumerate(self.deck):
            print(f"{i}. {card.__class__.__name__}")

    def print_hand(self):
        for i, card in enumerate(self.hand):
            print(f"{i}. {card.__class__.__name__}")

    def print_discard(self):
        for i, card in enumerate(self.discard):
            print(f"{i}. {card.__class__.__name__}")
