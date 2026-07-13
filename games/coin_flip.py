#!/usr/bin/env python3
"""Coin Flip Game - Flip a coin and guess the outcome."""

import random
import time


def main():
    print("\n" + "=" * 50)
    print("COIN FLIP".center(50))
    print("=" * 50)
    
    while True:
        print("\n1. Flip coin")
        print("2. Quit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '2':
            print("Goodbye!")
            break
        elif choice == '1':
            guess = input("\nHeads or Tails? (h/t): ").strip().lower()
            if guess not in ['h', 't']:
                print("Invalid choice. Please enter 'h' or 't'.")
                continue
            
            print("\nFlipping...")
            time.sleep(1)
            
            result = random.choice(['heads', 'tails'])
            print(f"It's {result}!")
            
            if (guess == 'h' and result == 'heads') or (guess == 't' and result == 'tails'):
                print("You win!")
            else:
                print("You lose!")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
