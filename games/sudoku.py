#!/usr/bin/env python3
"""
Sudoku Game for Terminal
Use arrow keys to move, number keys to enter values. Press 'q' to quit.
"""

import curses
import random
import time


# Sample Sudoku puzzles (0 represents empty cells)
SUDOKU_PUZZLES = [
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ],
    [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 0],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 7, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [3, 7, 0, 0, 0, 2, 0, 8, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 1, 0, 8, 0, 0, 0, 6, 5],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 6, 0, 0, 7, 2],
        [0, 0, 0, 3, 0, 5, 0, 1, 0],
    ],
]


def main():
    """Main function to run the sudoku game."""
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(100)
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Given
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Cursor
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)    # Error
    
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
    
    if sh < 20 or sw < 40:
        stdscr.addstr(sh // 2, sw // 2 - 10, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return
    
    # Select a random puzzle
    puzzle = random.choice(SUDOKU_PUZZLES)
    
    # Create working board
    board = [row[:] for row in puzzle]
    original = [row[:] for row in puzzle]
    
    # Cursor position
    cursor_y, cursor_x = 0, 0
    
    # Game state
    game_over = False
    
    # Game loop
    while not game_over:
        # Draw everything
        draw_game(stdscr, board, original, cursor_y, cursor_x, sh, sw)
        
        # Get input
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1
        elif key == curses.KEY_DOWN and cursor_y < 8:
            cursor_y += 1
        elif key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_RIGHT and cursor_x < 8:
            cursor_x += 1
        elif ord('1') <= key <= ord('9'):
            # Enter a number
            num = key - ord('1') + 1
            if original[cursor_y][cursor_x] == 0:  # Only allow changing empty cells
                board[cursor_y][cursor_x] = num
        elif key == ord(' '):
            # Clear cell
            if original[cursor_y][cursor_x] == 0:
                board[cursor_y][cursor_x] = 0
        elif key == ord('s'):
            # Solve (cheat)
            solve_sudoku(board)
        
        # Check if puzzle is solved
        if is_solved(board):
            game_over = True
    
    # Draw final state
    if game_over:
        draw_game(stdscr, board, original, cursor_y, cursor_x, sh, sw, solved=True)
        stdscr.addstr(sh - 3, 0, "CONGRATULATIONS! You solved the puzzle!")
    
    # Wait for user to press a key
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def is_solved(board):
    """Check if the puzzle is solved correctly."""
    # Check rows
    for row in board:
        if len(set(row)) != 9 or 0 in row:
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if len(set(column)) != 9 or 0 in column:
            return False
    
    # Check 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for row in range(box_row * 3, box_row * 3 + 3):
                for col in range(box_col * 3, box_col * 3 + 3):
                    box.append(board[row][col])
            if len(set(box)) != 9 or 0 in box:
                return False
    
    return True


def solve_sudoku(board):
    """Solve the sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    
    return False


def find_empty(board):
    """Find an empty cell (with value 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, row, col, num):
    """Check if placing num at (row, col) is valid."""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def draw_game(stdscr, board, original, cursor_y, cursor_x, sh, sw, solved=False):
    """Draw the game state."""
    stdscr.erase()
    
    # Draw instructions
    stdscr.addstr(0, 0, "Sudoku - Arrow keys to move, 1-9 to enter, Space to clear, Q to quit")
    
    # Calculate board position
    start_y = 2
    start_x = (sw - 9 * 4) // 2
    
    # Draw board
    for i in range(9):
        for j in range(9):
            y = start_y + i * 2
            x = start_x + j * 4
            
            value = board[i][j]
            
            # Determine color
            if original[i][j] != 0:
                color = 2  # Given
            else:
                color = 1  # Entered
            
            stdscr.attron(curses.color_pair(color))
            
            # Draw cell
            if value == 0:
                try:
                    stdscr.addstr(y, x, "    ")
                    stdscr.addstr(y + 1, x, "    ")
                except curses.error:
                    pass
            else:
                try:
                    stdscr.addstr(y, x + 1, str(value))
                except curses.error:
                    pass
            
            stdscr.attroff(curses.color_pair(color))
            
            # Draw cell borders
            if j < 8:
                try:
                    stdscr.addch(y, x + 3, '|')
                    stdscr.addch(y + 1, x + 3, '|')
                except curses.error:
                    pass
            
            if i < 8:
                try:
                    stdscr.addstr(y + 2, x, "----" if j % 3 == 2 else "----")
                except curses.error:
                    pass
    
    # Draw thick borders for 3x3 boxes
    for i in [3, 6]:
        y = start_y + i * 2 + 2
        try:
            stdscr.addstr(y, start_x, "----" * 9)
        except curses.error:
            pass
    
    for j in [3, 6]:
        x = start_x + j * 4 + 3
        for i in range(9):
            y = start_y + i * 2
            try:
                stdscr.addch(y, x, '+')
                stdscr.addch(y + 1, x, '+')
            except curses.error:
                pass
    
    # Draw cursor
    cursor_y_pos = start_y + cursor_y * 2
    cursor_x_pos = start_x + cursor_x * 4
    stdscr.attron(curses.color_pair(3) | curses.A_REVERSE)
    try:
        if board[cursor_y][cursor_x] == 0:
            stdscr.addstr(cursor_y_pos, cursor_x_pos, " ")
        else:
            stdscr.addstr(cursor_y_pos, cursor_x_pos + 1, str(board[cursor_y][cursor_x]))
    except curses.error:
        pass
    stdscr.attroff(curses.color_pair(3) | curses.A_REVERSE)
    
    # Draw game state
    if solved:
        stdscr.addstr(sh - 3, 0, "CONGRATULATIONS! You solved the puzzle!")
    
    stdscr.refresh()


if __name__ == "__main__":
    main()
