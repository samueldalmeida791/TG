#!/usr/bin/env python3
"""
Minesweeper Game for Terminal
Use arrow keys to move, space to reveal, 'f' to flag. Press 'q' to quit.
"""

import curses
import random
import time


def main():
    """Main function to run the minesweeper game."""
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
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Mine
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Flag
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Number
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Border
    
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
    
    # Game dimensions
    if sh < 15 or sw < 30:
        stdscr.addstr(sh // 2, sw // 2 - 10, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return
    
    # Difficulty selection
    stdscr.addstr(sh // 2 - 2, sw // 2 - 10, "Select difficulty:")
    stdscr.addstr(sh // 2 - 1, sw // 2 - 10, "1. Easy (8x8, 10 mines)")
    stdscr.addstr(sh // 2, sw // 2 - 10, "2. Medium (12x12, 30 mines)")
    stdscr.addstr(sh // 2 + 1, sw // 2 - 10, "3. Hard (16x16, 50 mines)")
    stdscr.refresh()
    
    difficulty = 1
    while True:
        key = stdscr.getch()
        if key == ord('1'):
            difficulty = 1
            break
        elif key == ord('2'):
            difficulty = 2
            break
        elif key == ord('3'):
            difficulty = 3
            break
        elif key == ord('q'):
            return
    
    # Set up game based on difficulty
    if difficulty == 1:
        rows, cols, mines = 8, 8, 10
    elif difficulty == 2:
        rows, cols, mines = 12, 12, 30
    else:
        rows, cols, mines = 16, 16, 50
    
    # Create game board
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    flagged = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Place mines
    place_mines(board, rows, cols, mines)
    
    # Calculate numbers
    calculate_numbers(board, rows, cols)
    
    # Cursor position
    cursor_y, cursor_x = 0, 0
    
    # Game state
    game_over = False
    game_won = False
    
    # Game loop
    while not game_over and not game_won:
        # Draw everything
        draw_game(stdscr, board, revealed, flagged, rows, cols, cursor_y, cursor_x, sh, sw)
        
        # Get input
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1
        elif key == curses.KEY_DOWN and cursor_y < rows - 1:
            cursor_y += 1
        elif key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_RIGHT and cursor_x < cols - 1:
            cursor_x += 1
        elif key == ord(' ') and not revealed[cursor_y][cursor_x] and not flagged[cursor_y][cursor_x]:
            # Reveal cell
            if board[cursor_y][cursor_x] == -1:
                # Hit a mine
                game_over = True
            else:
                reveal_cell(board, revealed, flagged, cursor_y, cursor_x, rows, cols)
        elif key == ord('f'):
            # Toggle flag
            if not revealed[cursor_y][cursor_x]:
                flagged[cursor_y][cursor_x] = not flagged[cursor_y][cursor_x]
        
        # Check if game is won
        game_won = check_win(revealed, flagged, board, rows, cols)
    
    # Draw final state
    draw_game(stdscr, board, revealed, flagged, rows, cols, cursor_y, cursor_x, sh, sw, game_over, game_won)
    
    # Show all mines if game over
    if game_over:
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    revealed[i][j] = True
        draw_game(stdscr, board, revealed, flagged, rows, cols, cursor_y, cursor_x, sh, sw, game_over, game_won)
    
    # Wait for user to press a key
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def place_mines(board, rows, cols, mines):
    """Place mines randomly on the board."""
    cells = [(i, j) for i in range(rows) for j in range(cols)]
    mine_cells = random.sample(cells, mines)
    
    for i, j in mine_cells:
        board[i][j] = -1


def calculate_numbers(board, rows, cols):
    """Calculate the numbers for each cell (count of adjacent mines)."""
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != -1:
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == -1:
                            count += 1
                board[i][j] = count


def reveal_cell(board, revealed, flagged, y, x, rows, cols):
    """Reveal a cell and recursively reveal adjacent cells if it's empty."""
    if y < 0 or y >= rows or x < 0 or x >= cols:
        return
    if revealed[y][x] or flagged[y][x]:
        return
    
    revealed[y][x] = True
    
    # If it's an empty cell, reveal adjacent cells
    if board[y][x] == 0:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                reveal_cell(board, revealed, flagged, y + dy, x + dx, rows, cols)


def check_win(revealed, flagged, board, rows, cols):
    """Check if the player has won (all non-mine cells revealed)."""
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != -1 and not revealed[i][j]:
                return False
            if board[i][j] == -1 and not flagged[i][j]:
                return False
    return True


def draw_game(stdscr, board, revealed, flagged, rows, cols, cursor_y, cursor_x, sh, sw, game_over=False, game_won=False):
    """Draw the game state."""
    stdscr.erase()
    
    # Draw instructions
    stdscr.addstr(0, 0, "Minesweeper - Arrow keys to move, Space to reveal, F to flag, Q to quit")
    
    # Calculate board position
    start_y = 2
    start_x = (sw - cols * 2) // 2
    
    # Draw board
    for i in range(rows):
        for j in range(cols):
            y = start_y + i * 2
            x = start_x + j * 2
            
            if revealed[i][j]:
                # Revealed cell
                if board[i][j] == -1:
                    stdscr.attron(curses.color_pair(2))
                    try:
                        stdscr.addch(y, x, '*')
                    except curses.error:
                        pass
                    stdscr.attroff(curses.color_pair(2))
                else:
                    if board[i][j] > 0:
                        stdscr.attron(curses.color_pair(4))
                        try:
                            stdscr.addch(y, x, str(board[i][j]))
                        except curses.error:
                            pass
                        stdscr.attroff(curses.color_pair(4))
                    else:
                        try:
                            stdscr.addch(y, x, ' ')
                        except curses.error:
                            pass
            elif flagged[i][j]:
                # Flagged cell
                stdscr.attron(curses.color_pair(3))
                try:
                    stdscr.addch(y, x, 'F')
                except curses.error:
                    pass
                stdscr.attroff(curses.color_pair(3))
            else:
                # Hidden cell
                try:
                    stdscr.addch(y, x, '.')
                except curses.error:
                    pass
    
    # Draw cursor
    cursor_y_pos = start_y + cursor_y * 2
    cursor_x_pos = start_x + cursor_x * 2
    stdscr.attron(curses.A_REVERSE)
    try:
        stdscr.addch(cursor_y_pos, cursor_x_pos, stdscr.inch(cursor_y_pos, cursor_x_pos))
    except curses.error:
        pass
    stdscr.attroff(curses.A_REVERSE)
    
    # Draw game state
    if game_over:
        stdscr.addstr(sh - 3, 0, "GAME OVER! You hit a mine!")
    elif game_won:
        stdscr.addstr(sh - 3, 0, "CONGRATULATIONS! You won!")
    
    stdscr.refresh()


if __name__ == "__main__":
    main()
