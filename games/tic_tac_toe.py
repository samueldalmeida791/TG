#!/usr/bin/env python3
"""
Tic Tac Toe for Terminal
2-player game. Players take turns entering row and column numbers (1-3).
"""

import sys


def main():
    """Main function to run the tic tac toe game."""
    print("\n" + "=" * 40)
    print("TIC TAC TOE".center(40))
    print("=" * 40)
    print("\nPlayers take turns entering row and column (1-3)")
    print("Player 1: X")
    print("Player 2: O")
    print("Enter 'quit' to exit")
    
    # Initialize board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 1
    
    # Game loop
    while True:
        # Draw board
        print("\n")
        print("   1   2   3")
        print(" +---+---+---+")
        for i, row in enumerate(board, 1):
            print(f"{i}| {' | '.join(row)} |{i}")
            print(" +---+---+---+")
        print("   1   2   3")
        
        # Get player input
        player_char = 'X' if current_player == 1 else 'O'
        print(f"\nPlayer {current_player}'s turn ({player_char})")
        
        while True:
            try:
                move = input("Enter row and column (e.g., '2 3'): ").strip().lower()
                if move == 'quit':
                    print("Game ended by user.")
                    return
                
                parts = move.split()
                if len(parts) != 2:
                    print("Please enter two numbers separated by a space.")
                    continue
                
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Row and column must be between 1 and 3.")
                    continue
                
                if board[row][col] != ' ':
                    print("That cell is already occupied.")
                    continue
                
                break
            except ValueError:
                print("Please enter valid numbers.")
        
        # Make move
        board[row][col] = player_char
        
        # Check for winner
        if check_winner(board, player_char):
            print("\n")
            print("   1   2   3")
            print(" +---+---+---+")
            for i, row in enumerate(board, 1):
                print(f"{i}| {' | '.join(row)} |{i}")
                print(" +---+---+---+")
            print("   1   2   3")
            print(f"\nPlayer {current_player} wins!")
            return
        
        # Check for draw
        if all(cell != ' ' for row in board for cell in row):
            print("\n")
            print("   1   2   3")
            print(" +---+---+---+")
            for i, row in enumerate(board, 1):
                print(f"{i}| {' | '.join(row)} |{i}")
                print(" +---+---+---+")
            print("   1   2   3")
            print("\nIt's a draw!")
            return
        
        # Switch players
        current_player = 2 if current_player == 1 else 1


def check_winner(board, player):
    """Check if the specified player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False


if __name__ == "__main__":
    main()
