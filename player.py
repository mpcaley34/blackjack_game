

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)
        print(f"{self.name} received: {card}")

    def initial_deal(self, deck):
        for _ in range(2):
            card = deck.deal(1)[0]
            self.add_card(card)

    def show_hand(self):
        print(f"{self.name}'s hand:", [str(card) for card in self.hand])

    def calculate_total(self):
        total = 0
        aces = 0

        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                total += 10
            elif card.rank == 'A':
                total += 11
                aces += 1
            else:
                total += int(card.rank)

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def make_decision(self):
        while True:
            decision = input(f"{self.name}, do you want to [hit] or [stand]? ")
            if decision in ['hit', 'stand']:
                return decision
            print("Invalid input. Please type 'hit' or 'stand'.")
