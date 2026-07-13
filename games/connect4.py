#!/usr/bin/env python3
"""
Connect 4 Game for Terminal
2-player game. Players take turns dropping discs into columns.
"""

import sys


def main():
    """Main function to run the connect 4 game."""
    print("\n" + "=" * 40)
    print("CONNECT 4".center(40))
    print("=" * 40)
    print("\nPlayers take turns dropping discs into columns (1-7)")
    print("Player 1: X")
    print("Player 2: O")
    print("Enter 'quit' to exit")
    
    # Initialize board
    rows = 6
    cols = 7
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    current_player = 1
    
    # Game loop
    while True:
        # Draw board
        print("\n")
        print("  " + "   ".join(str(i) for i in range(1, cols + 1)))
        print(" +" + "---+" * cols)
        for row in board:
            print(" | " + " | ".join(row) + " | ")
            print(" +" + "---+" * cols)
        print("  " + "   ".join(str(i) for i in range(1, cols + 1)))
        
        # Get player input
        player_char = 'X' if current_player == 1 else 'O'
        print(f"\nPlayer {current_player}'s turn ({player_char})")
        
        while True:
            try:
                col_input = input("Enter column number (1-7): ").strip().lower()
                if col_input == 'quit':
                    print("Game ended by user.")
                    return
                
                col = int(col_input) - 1
                
                if col < 0 or col >= cols:
                    print("Column must be between 1 and 7.")
                    continue
                
                # Find the first empty row in the column
                row = None
                for i in range(rows - 1, -1, -1):
                    if board[i][col] == ' ':
                        row = i
                        break
                
                if row is None:
                    print("That column is full.")
                    continue
                
                break
            except ValueError:
                print("Please enter a valid column number.")
        
        # Drop the disc
        board[row][col] = player_char
        
        # Check for winner
        if check_winner(board, player_char, row, col):
            print("\n")
            print("  " + "   ".join(str(i) for i in range(1, cols + 1)))
            print(" +" + "---+" * cols)
            for row in board:
                print(" | " + " | ".join(row) + " | ")
                print(" +" + "---+" * cols)
            print("  " + "   ".join(str(i) for i in range(1, cols + 1)))
            print(f"\nPlayer {current_player} wins!")
            return
        
        # Check for draw
        if all(cell != ' ' for row in board for cell in row):
            print("\n")
            print("  " + "   ".join(str(i) for i in range(1, cols + 1)))
            print(" +" + "---+" * cols)
            for row in board:
                print(" | " + " | ".join(row) + " | ")
                print(" +" + "---+" * cols)
            print("  " + "   ".join(str(i) for i in range(1, cols + 1)))
            print("\nIt's a draw!")
            return
        
        # Switch players
        current_player = 2 if current_player == 1 else 1


def check_winner(board, player, row, col):
    """Check if the specified player has won."""
    rows = len(board)
    cols = len(board[0])
    
    # Check horizontal
    count = 0
    for j in range(cols):
        if board[row][j] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    
    # Check vertical
    count = 0
    for i in range(rows):
        if board[i][col] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    
    # Check diagonal (top-left to bottom-right)
    count = 0
    for i, j in zip(range(rows), range(cols)):
        if 0 <= row - i == col - j < max(rows, cols) and board[row - i][col - j] == player:
            count += 1
            if count >= 4:
                return True
        else:
            break
    
    for i, j in zip(range(1, rows), range(1, cols)):
        if 0 <= row + i < rows and 0 <= col + j < cols and board[row + i][col + j] == player:
            count += 1
            if count >= 4:
                return True
        else:
            break
    
    # Check diagonal (top-right to bottom-left)
    count = 0
    for i, j in zip(range(rows), range(cols)):
        if 0 <= row - i < rows and 0 <= col + j < cols and board[row - i][col + j] == player:
            count += 1
            if count >= 4:
                return True
        else:
            break
    
    for i, j in zip(range(1, rows), range(1, cols)):
        if 0 <= row + i < rows and 0 <= col - j >= 0 and board[row + i][col - j] == player:
            count += 1
            if count >= 4:
                return True
        else:
            break
    
    return False


if __name__ == "__main__":
    main()
