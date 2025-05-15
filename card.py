import random


class Card:
    """Generates a card with suit and rank"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = ["A", "2", "3", "4", "5",
                      "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = self.generate_deck()

    def generate_deck(self):
        return [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = []
        if num_cards > len(self.cards):
            num_cards = len(self.cards)
        for _ in range(num_cards):
            if self.cards:
                dealt_cards.append(self.cards.pop())
        return dealt_cards

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
