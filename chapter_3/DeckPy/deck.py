from card import Card


class Deck:
    def __init__(self):
        self.cards = list()
        self.build_cards()

    def get(self, index: int):
        try:
            return self.cards.pop(index)
        except IndexError:
            return

    def add(self, card: Card):
        self.cards.append(card)

    def replace(self, index: int, card: Card):
        try:
            self.cards[index] = card
        except IndexError:
            pass

    def remove_from_front(self):
        try:
            return self.get(0)
        except IndexError:
            return

    def build_cards(self):
        suites = [
            Card.DIAMONDS,
            Card.HEARTS,
            Card.SPADES,
            Card.CLUBS
        ]
        ranks = [
            Card.TWO,
            Card.THREE,
            Card.FOUR,
            Card.FIVE,
            Card.SIX,
            Card.SEVEN, 
            Card.EIGHT,
            Card.NINE,
            Card.TEN,
            Card.JACK,
            Card.QUEEN,
            Card.KING,
            Card.ACE
        ]

        for suit in suites:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.replace(key, value)

    def __iter__(self):
        for card in self.cards:
            yield card

    def __str__(self):
        return ' '.join(
            str(card)
            for card in self
        )

    def __repr__(self):
        return str(self)