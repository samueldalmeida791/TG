#!/usr/bin/env python3
"""
Number Guessing Game
Guess the random number between 1 and 100.
"""

import random


def main():
    """Main function to run the number guessing game."""
    print("\n" + "=" * 50)
    print("NUMBER GUESSING GAME".center(50))
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}/{max_attempts}")
        
        try:
            guess = int(input("Your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                return
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nGame over! The number was {secret_number}.")


if __name__ == "__main__":
    main()
