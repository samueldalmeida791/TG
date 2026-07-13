#!/usr/bin/env python3
"""
Video Poker
5-card draw poker game.
"""

import random


# Card suits and ranks
SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Poker hand rankings
HAND_NAMES = [
    "High Card",
    "One Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
    "Royal Flush"
]


def create_deck():
    """Create a standard deck of 52 cards."""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    return deck


def deal_hand(deck, num_cards):
    """Deal a hand of cards from the deck."""
    hand = []
    for _ in range(num_cards):
        hand.append(deck.pop())
    return hand


def evaluate_hand(hand):
    """Evaluate a poker hand and return its rank (0-9)."""
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    
    # Count occurrences of each rank
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Check for flush
    flush = len(set(suits)) == 1
    
    # Check for straight
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                   '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    sorted_ranks = sorted([rank_values[r] for r in ranks])
    
    # Check for Ace-low straight (A, 2, 3, 4, 5)
    if set(sorted_ranks) == {2, 3, 4, 5, 14}:
        straight = True
    else:
        straight = (sorted_ranks[-1] - sorted_ranks[0] == 4 and 
                   len(set(sorted_ranks)) == 5)
    
    # Check for royal flush
    if flush and straight and sorted_ranks[0] == 10:
        return 9  # Royal Flush
    
    # Check for straight flush
    if flush and straight:
        return 8  # Straight Flush
    
    # Check for four of a kind
    if 4 in rank_counts.values():
        return 7  # Four of a Kind
    
    # Check for full house
    if sorted(rank_counts.values()) == [2, 3]:
        return 6  # Full House
    
    # Check for flush
    if flush:
        return 5  # Flush
    
    # Check for straight
    if straight:
        return 4  # Straight
    
    # Check for three of a kind
    if 3 in rank_counts.values():
        return 3  # Three of a Kind
    
    # Check for two pair
    if list(rank_counts.values()).count(2) == 2:
        return 2  # Two Pair
    
    # Check for one pair
    if 2 in rank_counts.values():
        return 1  # One Pair
    
    # High card
    return 0


def display_hand(hand):
    """Display a hand of cards."""
    cards = [f"{card[0]}{card[1]}" for card in hand]
    print("Your hand: " + " ".join(cards))


def main():
    """Main function to run the video poker game."""
    print("\n" + "=" * 50)
    print("VIDEO POKER".center(50))
    print("=" * 50)
    
    money = 100
    
    # Payout table
    payouts = {
        0: 0,   # High Card
        1: 1,   # One Pair
        2: 2,   # Two Pair
        3: 3,   # Three of a Kind
        4: 4,   # Straight
        5: 5,   # Flush
        6: 6,   # Full House
        7: 25,  # Four of a Kind
        8: 50,  # Straight Flush
        9: 250  # Royal Flush
    }
    
    while True:
        print(f"\nYou have ${money}")
        print("\n1. Play ($1 per hand)")
        print("2. Quit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '2':
            print(f"\nGoodbye! You're leaving with ${money}")
            break
        elif choice != '1':
            print("Invalid choice.")
            continue
        
        if money < 1:
            print("You don't have enough money to play!")
            break
        
        money -= 1
        
        # Create and shuffle deck
        deck = create_deck()
        random.shuffle(deck)
        
        # Deal initial hand
        hand = deal_hand(deck, 5)
        
        print("\n" + "=" * 50)
        display_hand(hand)
        
        # First evaluation
        hand_rank = evaluate_hand(hand)
        
        # Draw phase
        print("\nSelect cards to keep (1-5, separated by spaces, or 0 to keep all):")
        try:
            keep_indices = input("> ").strip()
            if keep_indices == '':
                keep_indices = '1 2 3 4 5'
            elif keep_indices == '0':
                keep_indices = ''
            
            keep_indices = [int(i) - 1 for i in keep_indices.split()]
            
            # Replace discarded cards
            new_hand = []
            for i in range(5):
                if i in keep_indices:
                    new_hand.append(hand[i])
                else:
                    if deck:
                        new_hand.append(deck.pop())
                    else:
                        new_hand.append(hand[i])
            
            hand = new_hand
            
            print("\n" + "=" * 50)
            display_hand(hand)
            
            # Final evaluation
            hand_rank = evaluate_hand(hand)
            
            print(f"\nYou have: {HAND_NAMES[hand_rank]}")
            
            # Calculate winnings
            winnings = payouts[hand_rank]
            money += winnings
            
            if winnings > 0:
                print(f"You win ${winnings}!")
            else:
                print("No payout.")
        except (ValueError, IndexError):
            print("Invalid input. Keeping all cards.")
            hand_rank = evaluate_hand(hand)
            print(f"\nYou have: {HAND_NAMES[hand_rank]}")
            winnings = payouts[hand_rank]
            money += winnings
            if winnings > 0:
                print(f"You win ${winnings}!")
        
        if money <= 0:
            print("\nYou're out of money! Game over.")
            break


if __name__ == "__main__":
    main()
