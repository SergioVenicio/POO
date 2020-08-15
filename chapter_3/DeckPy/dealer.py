from copy import copy
from deck import Deck
from random import shuffle


class Dealer:
    def __init__(self):
        self.deck = Deck()

    def shuffle(self):
        _deck = copy(self.deck)
        shuffle(_deck)
        self.deck = _deck

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.remove_from_front()

    def __str__(self):
        return str(self.deck)

    def __repr__(self):
        return str(self.deck)
