#!/usr/bin/env python3
"""
2048 Game for Terminal
Use arrow keys to move tiles. Press 'q' to quit.
"""

import curses
import random
import time


def main():
    """Main function to run the 2048 game."""
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(100)
    
    # Initialize colors
    curses.start_color()
    # Different colors for different tile values
    for i in range(1, 12):  # Up to 2048 (2^11)
        color_value = min(i * 20 + 100, 1000)
        curses.init_pair(i, color_value, curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_RED)  # For tiles > 2048
    
    try:
        run_game(stdscr)
    finally:
        # Clean up curses
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()


def run_game(stdscr):
    """Run the main game loop."""
    sh, sw = stdscr.getmaxyx()
    
    # Board dimensions
    board_size = 4
    cell_size = 5
    
    if sh < board_size * cell_size + 5 or sw < board_size * cell_size + 5:
        stdscr.addstr(sh // 2, sw // 2 - 10, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return
    
    # Initialize board
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    
    # Add initial tiles
    add_random_tile(board)
    add_random_tile(board)
    
    # Score
    score = 0
    
    # Game loop
    while True:
        # Draw everything
        draw_game(stdscr, board, score, board_size, cell_size, sh, sw)
        
        # Get input
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            moved = move_up(board)
        elif key == curses.KEY_DOWN:
            moved = move_down(board)
        elif key == curses.KEY_LEFT:
            moved = move_left(board)
        elif key == curses.KEY_RIGHT:
            moved = move_right(board)
        else:
            moved = False
        
        if moved:
            add_random_tile(board)
            
            # Check if game is over
            if is_game_over(board):
                draw_game(stdscr, board, score, board_size, cell_size, sh, sw)
                stdscr.addstr(sh - 1, 0, "GAME OVER! Press any key to exit...")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break
    
    # Wait for user to press a key
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def add_random_tile(board):
    """Add a random tile (2 or 4) to an empty cell."""
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4


def move_left(board):
    """Move all tiles to the left, merging when possible."""
    size = len(board)
    moved = False
    
    for row in board:
        # Remove zeros
        non_zero = [x for x in row if x != 0]
        
        # Merge adjacent equal values
        merged = []
        i = 0
        while i < len(non_zero):
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)
                i += 2
                moved = True
            else:
                merged.append(non_zero[i])
                i += 1
        
        # Pad with zeros
        merged += [0] * (size - len(merged))
        
        if merged != row:
            moved = True
            row[:] = merged
    
    return moved


def move_right(board):
    """Move all tiles to the right, merging when possible."""
    # Reverse each row, move left, then reverse back
    size = len(board)
    moved = False
    
    for row in board:
        original = row[:]
        row.reverse()
        row_moved = move_left([row])
        row.reverse()
        if row != original:
            moved = True
    
    return moved


def move_up(board):
    """Move all tiles up, merging when possible."""
    size = len(board)
    moved = False
    
    # Transpose the board (columns become rows)
    transposed = [[board[j][i] for j in range(size)] for i in range(size)]
    
    # Move left on transposed board
    for row in transposed:
        non_zero = [x for x in row if x != 0]
        merged = []
        i = 0
        while i < len(non_zero):
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)
                i += 2
                moved = True
            else:
                merged.append(non_zero[i])
                i += 1
        merged += [0] * (size - len(merged))
        if merged != row:
            moved = True
            row[:] = merged
    
    # Transpose back
    for i in range(size):
        for j in range(size):
            board[i][j] = transposed[j][i]
    
    return moved


def move_down(board):
    """Move all tiles down, merging when possible."""
    # Reverse each column, move up, then reverse back
    size = len(board)
    moved = False
    
    # Reverse each column
    for j in range(size):
        for i in range(size // 2):
            board[i][j], board[size - 1 - i][j] = board[size - 1 - i][j], board[i][j]
    
    # Move up
    if move_up(board):
        moved = True
    
    # Reverse each column back
    for j in range(size):
        for i in range(size // 2):
            board[i][j], board[size - 1 - i][j] = board[size - 1 - i][j], board[i][j]
    
    return moved


def is_game_over(board):
    """Check if the game is over (no more valid moves)."""
    size = len(board)
    
    # Check if there are any empty cells
    if any(board[i][j] == 0 for i in range(size) for j in range(size)):
        return False
    
    # Check if any merges are possible
    for i in range(size):
        for j in range(size):
            if j + 1 < size and board[i][j] == board[i][j + 1]:
                return False
            if i + 1 < size and board[i][j] == board[i + 1][j]:
                return False
    
    return True


def draw_game(stdscr, board, score, board_size, cell_size, sh, sw):
    """Draw the game state."""
    stdscr.erase()
    
    # Draw score
    stdscr.addstr(0, 0, f"2048 - Score: {score}")
    stdscr.addstr(1, 0, "Use arrow keys to move. Press 'q' to quit.")
    
    # Draw board
    start_y = 3
    start_x = 0
    
    for i in range(board_size):
        for j in range(board_size):
            value = board[i][j]
            y = start_y + i * cell_size
            x = start_x + j * cell_size
            
            # Draw cell
            if value == 0:
                stdscr.addstr(y, x, "     ")
                for k in range(1, cell_size):
                    stdscr.addstr(y + k, x, "|   |"[:cell_size])
                stdscr.addstr(y + cell_size, x, "     ")
            else:
                # Determine color based on value
                color_pair = get_color_pair(value)
                stdscr.attron(curses.color_pair(color_pair))
                
                # Draw cell with value
                value_str = str(value)
                padding = (cell_size - len(value_str)) // 2
                stdscr.addstr(y, x, " " * cell_size)
                for k in range(1, cell_size - 1):
                    if k == cell_size // 2:
                        stdscr.addstr(y + k, x + padding, value_str)
                    else:
                        stdscr.addstr(y + k, x, " " * cell_size)
                stdscr.addstr(y + cell_size - 1, x, " " * cell_size)
                
                stdscr.attroff(curses.color_pair(color_pair))
    
    stdscr.refresh()


def get_color_pair(value):
    """Get the color pair for a tile value."""
    if value == 0:
        return 0
    
    # Log2 of the value
    log_value = 0
    temp = value
    while temp > 1:
        temp //= 2
        log_value += 1
    
    # Cap at 11 (2048)
    if log_value >= 11:
        return 12
    return log_value


if __name__ == "__main__":
    main()
