from card import Deck
from player import Player
from dealer import Dealer


def main():
    print("Welcome to Blackjack!\n")

    # Setup
    deck = Deck()
    deck.shuffle()

    player = Player("Player 1")
    dealer = Dealer()

    # Initial Deal
    player.initial_deal(deck)
    dealer.initial_deal(deck)

    print()
    player.show_hand()
    dealer.show_hand(hidden=True)

    # Player's Turn
    while True:
        if player.calculate_total() >= 21:
            break

        decision = player.make_decision()
        if decision == 'hit':
            player.add_card(deck.deal(1)[0])
            player.show_hand()

            if player.calculate_total() > 21:
                print("Bust! You lose.")
                return
        elif decision == 'stand':
            break

    # Dealer's Turn
    print("\nDealer's turn...")
    dealer.show_hand(hidden=False)

    while dealer.calculate_total() < 17:
        print("Dealer hits.")
        dealer.add_card(deck.deal(1)[0])
        dealer.show_hand(hidden=False)

        if dealer.calculate_total() > 21:
            print("Dealer busts! You win.")
            return

    # Final Scores
    player_total = player.calculate_total()
    dealer_total = dealer.calculate_total()

    print(f"\nYour total: {player_total}")
    print(f"Dealer total: {dealer_total}")

    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a push!")


if __name__ == '__main__':
    main()
