class Card:
    DIAMONDS = '♦'
    HEARTS = '♥'
    SPADES = '♠'
    CLUBS = '♣'

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

    def __init__(self, suit: int, rank: int):
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def __str__(self):
        return f'{self.suit} {self.rank}'

    def __repr__(self):
        return str(self)
