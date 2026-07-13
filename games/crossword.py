#!/usr/bin/env python3
"""Crossword Puzzle - Word Game - Fill in the crossword."""

import random


# Simple crossword grid (5x5)
# 0 = empty, 1 = blocked, letter = filled
CROSSWORD_GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

# Words to place
WORDS = [
    ("apple", "Across", 0, 0, "right"),
    ("pearl", "Across", 2, 0, "right"),
    ("lemon", "Across", 4, 0, "right"),
    ("grape", "Down", 0, 0, "down"),
    ("plum", "Down", 0, 2, "down"),
    ("kiwi", "Down", 0, 4, "down"),
]


def create_puzzle():
    """Create a crossword puzzle."""
    grid = [row[:] for row in CROSSWORD_GRID]
    clues = {"Across": [], "Down": []}
    
    for word, direction, row, col, orient in WORDS:
        if direction == "Across":
            if orient == "right":
                for i, letter in enumerate(word):
                    if col + i < 5:
                        grid[row][col + i] = letter
            clues["Across"].append((word, f"Row {row + 1}, starts at column {col + 1}"))
        else:  # Down
            if orient == "down":
                for i, letter in enumerate(word):
                    if row + i < 5:
                        grid[row + i][col] = letter
            clues["Down"].append((word, f"Column {col + 1}, starts at row {row + 1}"))
    
    return grid, clues


def print_puzzle(grid, user_grid=None):
    """Print the crossword puzzle."""
    if user_grid is None:
        user_grid = [[" " for _ in range(5)] for _ in range(5)]
    
    print("\n   1 2 3 4 5")
    print("  +-+-+-+-+-+")
    for i, row in enumerate(grid):
        row_str = f"{i+1}|"
        for j, cell in enumerate(row):
            if cell == 1:  # Blocked
                row_str += "#|"
            else:
                row_str += f"{user_grid[i][j]}|"
        print(row_str)
        print("  +-+-+-+-+-+")


def main():
    """Main function to run the crossword puzzle game."""
    print("\n" + "=" * 50)
    print("CROSSWORD PUZZLE".center(50))
    print("=" * 50)
    
    grid, clues = create_puzzle()
    user_grid = [[" " for _ in range(5)] for _ in range(5)]
    
    # Mark blocked cells in user grid
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 1:
                user_grid[i][j] = "#"
    
    print_puzzle(grid, user_grid)
    
    # Print clues
    print("\nClues:")
    print("\nAcross:")
    for i, (word, clue) in enumerate(clues["Across"], 1):
        print(f"{i}. {clue}")
    
    print("\nDown:")
    for i, (word, clue) in enumerate(clues["Down"], 1):
        print(f"{i}. {clue}")
    
    # Game loop
    while True:
        print("\nEnter your answer in format: direction number word")
        print("Example: Across 1 apple")
        print("Or type 'check' to check, 'solve' to see solution, 'quit' to exit")
        
        command = input("\n> ").strip().lower()
        
        if command == 'quit':
            print("Goodbye!")
            break
        elif command == 'check':
            # Check answers
            correct = 0
            total = 0
            for i in range(5):
                for j in range(5):
                    if grid[i][j] != 1 and grid[i][j] != 0:
                        total += 1
                        if user_grid[i][j].lower() == grid[i][j].lower():
                            correct += 1
            print(f"\nScore: {correct}/{total} ({correct/total*100:.1f}%)")
        elif command == 'solve':
            print_puzzle(grid, grid)
        else:
            parts = command.split()
            if len(parts) < 3:
                print("Invalid format. Use: direction number word")
                continue
            
            direction = parts[0].capitalize()
            try:
                num = int(parts[1]) - 1
            except ValueError:
                print("Invalid number.")
                continue
            
            word = ' '.join(parts[2:]).upper()
            
            # Find the word in clues
            if direction in clues:
                if num < len(clues[direction]):
                    actual_word, clue = clues[direction][num]
                    if word == actual_word:
                        print("Correct!")
                        # Fill in the word
                        for word_data in WORDS:
                            w, d, row, col, orient = word_data
                            if w == actual_word and d == direction:
                                if d == "Across" and orient == "right":
                                    for i, letter in enumerate(word):
                                        if col + i < 5:
                                            user_grid[row][col + i] = letter
                                elif d == "Down" and orient == "down":
                                    for i, letter in enumerate(word):
                                        if row + i < 5:
                                            user_grid[row + i][col] = letter
                        print_puzzle(grid, user_grid)
                    else:
                        print(f"Incorrect. The correct word is: {actual_word}")
                else:
                    print("Invalid clue number.")
            else:
                print("Invalid direction. Use 'Across' or 'Down'.")


if __name__ == "__main__":
    main()
