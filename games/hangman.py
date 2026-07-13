#!/usr/bin/env python3
"""
Hangman Game for Terminal
Guess the word before the hangman is complete!
"""

import random
import sys


# Word categories
WORD_CATEGORIES = {
    "Animals": ["elephant", "giraffe", "kangaroo", "rhinoceros", "hippopotamus", 
                "chameleon", "octopus", "penguin", "flamingo", "crocodile"],
    "Countries": ["canada", "japan", "brazil", "australia", "germany", 
                  "indonesia", "madagascar", "luxembourg", "switzerland", "vatican"],
    "Food": ["spaghetti", "hamburger", "chocolate", "strawberry", "watermelon",
             "sandwich", "pizza", "sushi", "broccoli", "tomato"],
    "Movies": ["titanic", "avatar", "inception", "matrix", "frozen",
               "shrek", "joker", "parasite", "forrest", "bambi"],
    "Programming": ["python", "javascript", "algorithm", "function", "variable",
                    "compiler", "database", "framework", "library", "recursion"],
}

# Hangman stages
HANGMAN_STAGES = [
    """
    +---+
    |   |
        |
        |
        |
        |
    ========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    ========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    ========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    ========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    ========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ========
    """,
]


def main():
    """Main function to run the hangman game."""
    print("\n" + "=" * 50)
    print("HANGMAN".center(50))
    print("=" * 50)
    
    # Select category
    print("\nSelect a category:")
    for i, category in enumerate(WORD_CATEGORIES.keys(), 1):
        print(f"{i}. {category}")
    print(f"{len(WORD_CATEGORIES) + 1}. Random")
    
    while True:
        try:
            choice = input("Enter your choice (1-{}): ".format(len(WORD_CATEGORIES) + 1))
            choice = int(choice)
            if 1 <= choice <= len(WORD_CATEGORIES) + 1:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")
    
    if choice == len(WORD_CATEGORIES) + 1:
        category = random.choice(list(WORD_CATEGORIES.keys()))
        word = random.choice(WORD_CATEGORIES[category])
    else:
        category = list(WORD_CATEGORIES.keys())[choice - 1]
        word = random.choice(WORD_CATEGORIES[category])
    
    print(f"\nCategory: {category}")
    print(f"The word has {len(word)} letters.")
    
    # Game state
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(HANGMAN_STAGES) - 1
    
    # Game loop
    while wrong_guesses < max_wrong_guesses:
        # Display hangman
        print(HANGMAN_STAGES[wrong_guesses])
        
        # Display word with guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())
        
        # Display guessed letters
        guessed = sorted(guessed_letters)
        print(f"\nGuessed letters: {' '.join(guessed)}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
        
        # Get user input
        while True:
            guess = input("\nGuess a letter: ").lower().strip()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a letter.")
            elif guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                break
        
        guessed_letters.add(guess)
        
        # Check if letter is in word
        if guess not in word:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")
        
        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"\nThe word was: {word}")
            print("\nCONGRATULATIONS! You won!")
            return
        
        print()
    
    # Game over
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\nThe word was: {word}")
    print("\nGAME OVER! The hangman is complete.")


if __name__ == "__main__":
    main()
