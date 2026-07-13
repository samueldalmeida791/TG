#!/usr/bin/env python3
"""Anagrams - Word Game - Rearrange letters to form words."""

import random


# List of words for anagrams
WORD_LIST = [
    "listen", "silent", "aster", "stare", "rate", "tear", "heart", "earth",
    "angel", "glean", "large", "regal", "elbow", "below", "debit", "bided",
    "dusty", "study", "night", "thing", "inch", "chin", "brag", "grab",
    "cat", "act", "dog", "god", "save", "vase", "state", "taste", "great", "grate",
    "least", "stale", "slate", "tales", "leapt", "plate", "pleat", "pasta", "taps",
    "stop", "opts", "pots", "spot", "top", "part", "rapt", "trap", "apt", "pat",
    "bake", "beak", "brake", "break", "crate", "trace", "react", "cater",
    "teach", "cheat", "water", "waste", "stew", "west", "tame", "meat",
    "name", "mean", "amen", "man", "men", "note", "tone", "ten", "net",
    "read", "dare", "dear", "reed", "bead", "bade", "bread", "beard", "brave",
    "cave", "veca", "race", "care", "acre", "fear", "fare", "reaf", "leaf",
]


def get_anagrams(word):
    """Get all anagrams of a word from the word list."""
    word_sorted = sorted(word.lower())
    anagrams = []
    for w in WORD_LIST:
        if w != word and sorted(w.lower()) == word_sorted:
            anagrams.append(w)
    return anagrams


def main():
    """Main function to run the anagrams game."""
    print("\n" + "=" * 50)
    print("ANAGRAMS".center(50))
    print("=" * 50)
    print("\nRearrange the letters to form a valid word.")
    print("Type 'quit' to exit.")
    
    score = 0
    
    while True:
        # Select a random word
        word = random.choice(WORD_LIST)
        anagrams = get_anagrams(word)
        
        if not anagrams:
            continue
        
        # Shuffle the letters
        shuffled = list(word)
        random.shuffle(shuffled)
        shuffled_word = ''.join(shuffled)
        
        print(f"\nAnagram: {shuffled_word}")
        print(f"Score: {score}")
        
        answer = input("Your guess: ").strip().lower()
        
        if answer == 'quit':
            print(f"\nGoodbye! Final score: {score}")
            break
        
        if answer in [word] + anagrams:
            print(f"Correct! '{answer}' is a valid word.")
            score += 1
        else:
            print(f"Incorrect. Valid words: {', '.join([word] + anagrams)}")
            score = max(0, score - 1)


if __name__ == "__main__":
    main()
