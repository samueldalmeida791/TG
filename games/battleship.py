#!/usr/bin/env python3
"""
Battleship Game for Terminal
2-player game. Players take turns guessing coordinates to sink ships.
"""

import random
import sys


def main():
    """Main function to run the battleship game."""
    print("\n" + "=" * 50)
    print("BATTLESHIP".center(50))
    print("=" * 50)
    print("\n1. Player vs Computer")
    print("2. Computer vs Computer (Watch)")
    print("3. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice == '1':
                player_vs_computer()
                break
            elif choice == '2':
                computer_vs_computer()
                break
            elif choice == '3':
                print("Goodbye!")
                return
            else:
                print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return


def player_vs_computer():
    """Player vs Computer game mode."""
    print("\n" + "=" * 50)
    print("PLAYER VS COMPUTER".center(50))
    print("=" * 50)
    
    # Create boards
    player_board = create_board()
    computer_board = create_board()
    
    # Place ships
    print("\nPlacing your ships...")
    place_player_ships(player_board)
    
    print("\nComputer is placing its ships...")
    place_computer_ships(computer_board)
    
    # Create tracking boards
    player_guesses = create_board()
    computer_guesses = create_board()
    
    # Game loop
    while True:
        # Player's turn
        print("\n" + "=" * 50)
        print("YOUR TURN".center(50))
        print("=" * 50)
        print("\nYour board:")
        print_board(player_board, show_ships=True)
        print("\nYour guesses on computer's board:")
        print_board(player_guesses, show_ships=False)
        
        # Get player's guess
        while True:
            try:
                guess = input("\nEnter your guess (e.g., 'A5'): ").strip().upper()
                if len(guess) < 2:
                    print("Please enter a valid coordinate (e.g., 'A5').")
                    continue
                
                col = ord(guess[0]) - ord('A')
                row = int(guess[1:]) - 1
                
                if col < 0 or col >= 10 or row < 0 or row >= 10:
                    print("Coordinate out of range. Please try again.")
                    continue
                
                if player_guesses[row][col] != ' ':
                    print("You already guessed that coordinate. Please try again.")
                    continue
                
                break
            except ValueError:
                print("Please enter a valid coordinate (e.g., 'A5').")
        
        # Process player's guess
        if computer_board[row][col] == 'S':
            player_guesses[row][col] = 'H'
            computer_board[row][col] = 'H'
            print("HIT!")
        else:
            player_guesses[row][col] = 'M'
            print("MISS!")
        
        # Check if player won
        if check_win(computer_board):
            print("\n" + "=" * 50)
            print("YOU WIN!".center(50))
            print("=" * 50)
            print("\nComputer's board:")
            print_board(computer_board, show_ships=True)
            return
        
        # Computer's turn
        print("\n" + "=" * 50)
        print("COMPUTER'S TURN".center(50))
        print("=" * 50)
        
        # Computer makes a guess
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            if computer_guesses[row][col] == ' ':
                break
        
        print(f"\nComputer guesses: {chr(col + ord('A'))}{row + 1}")
        
        # Process computer's guess
        if player_board[row][col] == 'S':
            computer_guesses[row][col] = 'H'
            player_board[row][col] = 'H'
            print("Computer HIT your ship!")
        else:
            computer_guesses[row][col] = 'M'
            print("Computer MISSED!")
        
        # Check if computer won
        if check_win(player_board):
            print("\n" + "=" * 50)
            print("COMPUTER WINS!".center(50))
            print("=" * 50)
            print("\nYour board:")
            print_board(player_board, show_ships=True)
            return


def computer_vs_computer():
    """Computer vs Computer game mode (watch mode)."""
    print("\n" + "=" * 50)
    print("COMPUTER VS COMPUTER".center(50))
    print("=" * 50)
    
    # Create boards
    board1 = create_board()
    board2 = create_board()
    
    # Place ships
    print("\nPlacing ships...")
    place_computer_ships(board1)
    place_computer_ships(board2)
    
    # Create tracking boards
    guesses1 = create_board()
    guesses2 = create_board()
    
    # Game loop
    turn = 0
    while True:
        turn += 1
        print(f"\n{'=' * 50}")
        print(f"TURN {turn}".center(50))
        print("=" * 50)
        
        # Computer 1's turn
        print("\nComputer 1's turn:")
        row, col = make_smart_guess(board2, guesses1)
        print(f"Computer 1 guesses: {chr(col + ord('A'))}{row + 1}")
        
        if board2[row][col] == 'S':
            guesses1[row][col] = 'H'
            board2[row][col] = 'H'
            print("HIT!")
        else:
            guesses1[row][col] = 'M'
            print("MISS!")
        
        # Check if computer 1 won
        if check_win(board2):
            print("\n" + "=" * 50)
            print("COMPUTER 1 WINS!".center(50))
            print("=" * 50)
            return
        
        # Computer 2's turn
        print("\nComputer 2's turn:")
        row, col = make_smart_guess(board1, guesses2)
        print(f"Computer 2 guesses: {chr(col + ord('A'))}{row + 1}")
        
        if board1[row][col] == 'S':
            guesses2[row][col] = 'H'
            board1[row][col] = 'H'
            print("HIT!")
        else:
            guesses2[row][col] = 'M'
            print("MISS!")
        
        # Check if computer 2 won
        if check_win(board1):
            print("\n" + "=" * 50)
            print("COMPUTER 2 WINS!".center(50))
            print("=" * 50)
            return
        
        # Small delay
        input("Press Enter to continue...")


def create_board():
    """Create an empty 10x10 board."""
    return [[' ' for _ in range(10)] for _ in range(10)]


def place_player_ships(board):
    """Let the player place their ships."""
    ships = [
        ("Carrier", 5),
        ("Battleship", 4),
        ("Cruiser", 3),
        ("Submarine", 3),
        ("Destroyer", 2),
    ]
    
    for ship_name, ship_size in ships:
        print(f"\nPlacing {ship_name} ({ship_size} cells):")
        print_board(board, show_ships=True)
        
        while True:
            try:
                direction = input(f"Direction (H for horizontal, V for vertical): ").strip().upper()
                if direction not in ['H', 'V']:
                    print("Please enter 'H' or 'V'.")
                    continue
                
                start = input(f"Starting position (e.g., 'A5'): ").strip().upper()
                if len(start) < 2:
                    print("Please enter a valid coordinate (e.g., 'A5').")
                    continue
                
                col = ord(start[0]) - ord('A')
                row = int(start[1:]) - 1
                
                if col < 0 or col >= 10 or row < 0 or row >= 10:
                    print("Coordinate out of range. Please try again.")
                    continue
                
                # Check if ship fits
                if direction == 'H':
                    if col + ship_size > 10:
                        print("Ship doesn't fit. Please try again.")
                        continue
                    cells = [(row, col + i) for i in range(ship_size)]
                else:  # V
                    if row + ship_size > 10:
                        print("Ship doesn't fit. Please try again.")
                        continue
                    cells = [(row + i, col) for i in range(ship_size)]
                
                # Check if cells are empty
                valid = True
                for r, c in cells:
                    if board[r][c] != ' ':
                        valid = False
                        break
                
                if not valid:
                    print("Ship overlaps with another ship. Please try again.")
                    continue
                
                # Place ship
                for r, c in cells:
                    board[r][c] = 'S'
                
                break
            except ValueError:
                print("Please enter a valid coordinate (e.g., 'A5').")


def place_computer_ships(board):
    """Randomly place computer's ships."""
    ships = [
        ("Carrier", 5),
        ("Battleship", 4),
        ("Cruiser", 3),
        ("Submarine", 3),
        ("Destroyer", 2),
    ]
    
    for ship_name, ship_size in ships:
        while True:
            direction = random.choice(['H', 'V'])
            if direction == 'H':
                col = random.randint(0, 10 - ship_size)
                row = random.randint(0, 9)
                cells = [(row, col + i) for i in range(ship_size)]
            else:  # V
                row = random.randint(0, 10 - ship_size)
                col = random.randint(0, 9)
                cells = [(row + i, col) for i in range(ship_size)]
            
            # Check if cells are empty
            valid = True
            for r, c in cells:
                if board[r][c] != ' ':
                    valid = False
                    break
            
            if valid:
                # Place ship
                for r, c in cells:
                    board[r][c] = 'S'
                break


def make_smart_guess(board, guesses):
    """Make a smart guess based on previous hits."""
    # First, try to find adjacent cells to hits
    hits = [(i, j) for i in range(10) for j in range(10) if guesses[i][j] == 'H']
    
    if hits:
        # Try adjacent cells to hits
        adjacent = []
        for i, j in hits:
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < 10 and 0 <= nj < 10 and guesses[ni][nj] == ' ':
                    adjacent.append((ni, nj))
        
        if adjacent:
            return random.choice(adjacent)
    
    # Otherwise, make a random guess
    empty_cells = [(i, j) for i in range(10) for j in range(10) if guesses[i][j] == ' ']
    return random.choice(empty_cells)


def check_win(board):
    """Check if all ships on the board are sunk."""
    for i in range(10):
        for j in range(10):
            if board[i][j] == 'S':
                return False
    return True


def print_board(board, show_ships=False):
    """Print the board."""
    print("\n   A B C D E F G H I J")
    print("  +" + "-" * 19 + "+ ")
    
    for i, row in enumerate(board):
        row_str = f"{i+1:2d}|"
        for cell in row:
            if show_ships and cell == 'S':
                row_str += " S"
            elif cell == 'H':
                row_str += " H"
            elif cell == 'M':
                row_str += " M"
            else:
                row_str += "  "
        row_str += f" |{i+1}"
        print(row_str)
    
    print("  +" + "-" * 19 + "+ ")
    print("   A B C D E F G H I J")


if __name__ == "__main__":
    main()
