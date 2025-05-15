class Dealer:
    def __init__(self):
        self.hand = []
        self.hidden_second_card = True

    def add_card(self, card):
        self.hand.append(card)
        print(f"Dealer received: {card}")

    def initial_deal(self, deck):
        for _ in range(2):
            card = deck.deal(1)[0]
            self.add_card(card)
        print("Dealer has been dealt 2 cards.")

    def show_hand(self, hidden=False):
        if hidden and len(self.hand) >= 2:
            print(f"Dealer's hand: [{self.hand[0]}, Hidden]")
        else:
            print("Dealer's hand:", [str(card) for card in self.hand])

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

        # Adjust for aces if total is over 21
        while total >= 21 and aces:
            toatl -= 10
            aces -= 1

        return total
