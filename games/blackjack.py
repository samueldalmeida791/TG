#!/usr/bin/env python3
"""
Blackjack (21)
Card game against the dealer.
"""

import random


# Card suits and ranks
SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def create_deck():
    """Create a standard deck of 52 cards."""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    return deck


def get_card_value(card):
    """Get the value of a card."""
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11  # Ace is 11 by default, will be adjusted if needed
    else:
        return int(rank)


def calculate_hand_value(hand):
    """Calculate the total value of a hand, adjusting for Aces."""
    total = sum(get_card_value(card) for card in hand)
    
    # Adjust for Aces if total is over 21
    aces = sum(1 for card in hand if card[0] == 'A')
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    
    return total


def display_hand(hand, label):
    """Display a hand of cards."""
    cards = [f"{card[0]}{card[1]}" for card in hand]
    print(f"{label}: {' '.join(cards)}")


def main():
    """Main function to run the blackjack game."""
    print("\n" + "=" * 50)
    print("BLACKJACK (21)".center(50))
    print("=" * 50)
    
    money = 100
    
    while True:
        print(f"\nYou have ${money}")
        print("\n1. Play")
        print("2. Quit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '2':
            print(f"\nGoodbye! You're leaving with ${money}")
            break
        elif choice != '1':
            print("Invalid choice.")
            continue
        
        # Place bet
        while True:
            try:
                bet = int(input("\nPlace your bet: $"))
                if bet < 1 or bet > money:
                    print(f"Bet must be between $1 and ${money}")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Create and shuffle deck
        deck = create_deck()
        random.shuffle(deck)
        
        # Deal initial cards
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        
        # Check for blackjack
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        
        print("\n" + "=" * 50)
        display_hand(player_hand, "Your hand")
        print(f"Your total: {player_value}")
        display_hand([dealer_hand[0]], "Dealer's hand")
        
        if player_value == 21:
            print("\nBLACKJACK! You win!")
            money += int(bet * 1.5)
            continue
        
        # Player's turn
        while True:
            print("\n1. Hit")
            print("2. Stand")
            
            choice = input("\nYour choice: ").strip()
            
            if choice == '1':
                player_hand.append(deck.pop())
                player_value = calculate_hand_value(player_hand)
                
                print("\n" + "=" * 50)
                display_hand(player_hand, "Your hand")
                print(f"Your total: {player_value}")
                display_hand([dealer_hand[0]], "Dealer's hand")
                
                if player_value > 21:
                    print("\nBust! You lose.")
                    money -= bet
                    break
            elif choice == '2':
                break
            else:
                print("Invalid choice.")
        
        if player_value > 21:
            continue
        
        # Dealer's turn
        print("\n" + "=" * 50)
        display_hand(player_hand, "Your hand")
        print(f"Your total: {player_value}")
        display_hand(dealer_hand, "Dealer's hand")
        print(f"Dealer's total: {dealer_value}")
        
        while dealer_value < 17:
            dealer_hand.append(deck.pop())
            dealer_value = calculate_hand_value(dealer_hand)
            print(f"\nDealer hits: {dealer_hand[-1][0]}{dealer_hand[-1][1]}")
            print(f"Dealer's total: {dealer_value}")
        
        # Determine winner
        print("\n" + "=" * 50)
        display_hand(player_hand, "Your hand")
        print(f"Your total: {player_value}")
        display_hand(dealer_hand, "Dealer's hand")
        print(f"Dealer's total: {dealer_value}")
        
        if dealer_value > 21:
            print("\nDealer busts! You win!")
            money += bet
        elif dealer_value > player_value:
            print("\nDealer wins!")
            money -= bet
        elif dealer_value < player_value:
            print("\nYou win!")
            money += bet
        else:
            print("\nPush! It's a tie.")
        
        if money <= 0:
            print("\nYou're out of money! Game over.")
            break


if __name__ == "__main__":
    main()
