#!/usr/bin/env python3
"""
Memory Card Game for Terminal
Match pairs of cards by remembering their positions.
"""

import random
import time
import sys


def main():
    """Main function to run the memory game."""
    print("\n" + "=" * 50)
    print("MEMORY CARD GAME".center(50))
    print("=" * 50)
    print("\nSelect difficulty:")
    print("1. Easy (4x4 grid, 8 pairs)")
    print("2. Medium (6x6 grid, 18 pairs)")
    print("3. Hard (8x8 grid, 32 pairs)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice == '1':
                rows, cols = 4, 4
                break
            elif choice == '2':
                rows, cols = 6, 6
                break
            elif choice == '3':
                rows, cols = 8, 8
                break
            else:
                print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return
    
    # Create cards
    pairs = (rows * cols) // 2
    symbols = [chr(i) for i in range(65, 65 + pairs)]  # A, B, C, ...
    cards = symbols + symbols
    random.shuffle(cards)
    
    # Create board
    board = [cards[i * cols:(i + 1) * cols] for i in range(rows)]
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Game state
    first_card = None
    second_card = None
    matches = 0
    moves = 0
    
    # Game loop
    while matches < pairs:
        # Draw board
        print("\n" + "=" * 50)
        print(f"Moves: {moves} | Matches: {matches}/{pairs}".center(50))
        print("=" * 50)
        print_board(board, revealed, rows, cols)
        
        # Get first card
        if first_card is None:
            print("\nSelect first card (e.g., 'A1'):")
            while True:
                try:
                    pos = input("> ").strip().upper()
                    if len(pos) < 2:
                        print("Please enter a valid position (e.g., 'A1').")
                        continue
                    
                    col = ord(pos[0]) - ord('A')
                    row = int(pos[1:]) - 1
                    
                    if col < 0 or col >= cols or row < 0 or row >= rows:
                        print("Position out of range. Please try again.")
                        continue
                    
                    if revealed[row][col]:
                        print("That card is already revealed. Please try again.")
                        continue
                    
                    first_card = (row, col)
                    revealed[row][col] = True
                    break
                except ValueError:
                    print("Please enter a valid position (e.g., 'A1').")
        else:
            # Get second card
            print("\nSelect second card (e.g., 'B2'):")
            while True:
                try:
                    pos = input("> ").strip().upper()
                    if len(pos) < 2:
                        print("Please enter a valid position (e.g., 'B2').")
                        continue
                    
                    col = ord(pos[0]) - ord('A')
                    row = int(pos[1:]) - 1
                    
                    if col < 0 or col >= cols or row < 0 or row >= rows:
                        print("Position out of range. Please try again.")
                        continue
                    
                    if revealed[row][col]:
                        print("That card is already revealed. Please try again.")
                        continue
                    
                    if (row, col) == first_card:
                        print("You can't select the same card twice. Please try again.")
                        continue
                    
                    second_card = (row, col)
                    revealed[row][col] = True
                    break
                except ValueError:
                    print("Please enter a valid position (e.g., 'B2').")
        
        # Check for match
        moves += 1
        row1, col1 = first_card
        row2, col2 = second_card
        
        print("\n" + "=" * 50)
        print(f"Moves: {moves} | Matches: {matches}/{pairs}".center(50))
        print("=" * 50)
        print_board(board, revealed, rows, cols)
        
        if board[row1][col1] == board[row2][col2]:
            print("\nMATCH!")
            matches += 1
        else:
            print("\nNo match!")
            # Hide cards after a delay
            time.sleep(1)
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        
        # Reset selection
        first_card = None
        second_card = None
    
    # Game won
    print("\n" + "=" * 50)
    print("CONGRATULATIONS! You won!".center(50))
    print(f"Total moves: {moves}".center(50))
    print("=" * 50)
    print_board(board, revealed, rows, cols)


def print_board(board, revealed, rows, cols):
    """Print the game board."""
    # Print column headers
    print("\n    " + "   ".join(chr(ord('A') + i) for i in range(cols)))
    print("   " + "----" * cols)
    
    for i in range(rows):
        row_str = f"{i+1:2d} |"
        for j in range(cols):
            if revealed[i][j]:
                row_str += f" {board[i][j]} |"
            else:
                row_str += " ? |"
        print(row_str)
        print("   " + "----" * cols)


if __name__ == "__main__":
    main()
