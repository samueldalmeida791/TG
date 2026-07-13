#!/usr/bin/env python3
"""
Rock Paper Scissors
Classic hand game against the computer.
"""

import random


def main():
    """Main function to run the rock paper scissors game."""
    print("\n" + "=" * 50)
    print("ROCK PAPER SCISSORS".center(50))
    print("=" * 50)
    
    choices = ['rock', 'paper', 'scissors']
    score = {'player': 0, 'computer': 0, 'ties': 0}
    
    while True:
        print(f"\nScore: Player {score['player']} - {score['computer']} Computer (Ties: {score['ties']})")
        print("\nChoose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("0. Quit")
        
        try:
            choice = input("\nYour choice: ").strip()
            if choice == '0':
                print("\nFinal Score:")
                print(f"Player: {score['player']} | Computer: {score['computer']} | Ties: {score['ties']}")
                print("Goodbye!")
                break
            
            player_choice = choices[int(choice) - 1]
            computer_choice = random.choice(choices)
            
            print(f"\nYou chose: {player_choice.capitalize()}")
            print(f"Computer chose: {computer_choice.capitalize()}")
            
            # Determine winner
            if player_choice == computer_choice:
                print("It's a tie!")
                score['ties'] += 1
            elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                 (player_choice == 'paper' and computer_choice == 'rock') or \
                 (player_choice == 'scissors' and computer_choice == 'paper'):
                print("You win!")
                score['player'] += 1
            else:
                print("Computer wins!")
                score['computer'] += 1
        except (ValueError, IndexError):
            print("Invalid choice. Please enter 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
