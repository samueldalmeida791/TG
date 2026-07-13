#!/usr/bin/env python3
"""High Low Game - Guess if the next card is higher or lower."""

import random


SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def get_rank_value(rank):
    """Get the numerical value of a card rank."""
    if rank == 'A':
        return 1
    elif rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'K':
        return 13
    else:
        return int(rank)


def main():
    print("\n" + "=" * 50)
    print("HIGH LOW GAME".center(50))
    print("=" * 50)
    print("\nGuess if the next card is higher or lower than the current card.")
    print("Ace is low (1), Jack is 11, Queen is 12, King is 13.")
    
    # Create deck
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    
    random.shuffle(deck)
    
    score = 0
    current_card = deck.pop()
    
    while deck:
        rank, suit = current_card
        value = get_rank_value(rank)
        
        print(f"\nCurrent card: {rank}{suit} (Value: {value})")
        print(f"Score: {score}")
        
        guess = input("Higher or Lower? (h/l): ").strip().lower()
        
        if guess not in ['h', 'l']:
            print("Invalid choice. Please enter 'h' or 'l'.")
            continue
        
        next_card = deck.pop()
        next_rank, next_suit = next_card
        next_value = get_rank_value(next_rank)
        
        print(f"Next card: {next_rank}{next_suit} (Value: {next_value})")
        
        if (guess == 'h' and next_value > value) or (guess == 'l' and next_value < value):
            print("Correct!")
            score += 1
        elif next_value == value:
            print("It's the same value! No change.")
        else:
            print("Wrong!")
            score -= 1
        
        current_card = next_card
    
    print(f"\nGame over! Final score: {score}")


if __name__ == "__main__":
    main()
