#!/usr/bin/env python3
"""
Tetris Game for Terminal
Use arrow keys to move, space to rotate, 'q' to quit.
"""

import curses
import random
import time


# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]

# Colors for each shape
COLORS = [
    curses.COLOR_CYAN,    # I
    curses.COLOR_YELLOW,  # O
    curses.COLOR_MAGENTA, # T
    curses.COLOR_BLUE,    # L
    curses.COLOR_GREEN,   # J
    curses.COLOR_RED,     # S
    curses.COLOR_WHITE,   # Z
]


def main():
    """Main function to run the tetris game."""
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(100)
    
    # Initialize colors
    curses.start_color()
    for i, color in enumerate(COLORS, 1):
        curses.init_pair(i, color, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Border
    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Text
    
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
    board_h, board_w = 20, 10
    info_w = 20
    
    if sw < board_w + info_w + 2 or sh < board_h + 2:
        stdscr.addstr(sh // 2, sw // 2 - 10, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return
    
    # Create windows
    board_win = curses.newwin(board_h, board_w, 1, 1)
    board_win.keypad(True)
    board_win.timeout(100)
    
    info_win = curses.newwin(board_h, info_w, 1, board_w + 2)
    
    # Initialize game state
    board = [[0 for _ in range(board_w)] for _ in range(board_h)]
    current_piece = None
    next_piece = None
    current_x, current_y = 0, 0
    score = 0
    level = 1
    lines_cleared = 0
    game_over_flag = False
    
    # Create first pieces
    new_piece(board, board_w, board_h)
    
    # Game loop
    fall_time = 0
    fall_speed = 0.5  # seconds
    last_fall = time.time()
    
    while not game_over_flag:
        # Get current time
        current_time = time.time()
        
        # Handle falling
        if current_time - last_fall > fall_speed:
            if not move_piece(board, current_piece, current_x, current_y, 
                             current_x, current_y + 1, board_w, board_h):
                # Piece can't move down, lock it in place
                lock_piece(board, current_piece, current_x, current_y)
                
                # Check for completed lines
                lines = check_lines(board, board_h, board_w)
                lines_cleared += lines
                score += calculate_score(lines, level)
                
                # Update level
                level = lines_cleared // 10 + 1
                fall_speed = max(0.05, 0.5 - (level - 1) * 0.05)
                
                # Create new piece
                if not new_piece(board, board_w, board_h):
                    game_over_flag = True
            
            last_fall = current_time
        
        # Get input
        key = board_win.getch()
        
        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT:
            move_piece(board, current_piece, current_x, current_y,
                      current_x - 1, current_y, board_w, board_h)
        elif key == curses.KEY_RIGHT:
            move_piece(board, current_piece, current_x, current_y,
                      current_x + 1, current_y, board_w, board_h)
        elif key == curses.KEY_DOWN:
            move_piece(board, current_piece, current_x, current_y,
                      current_x, current_y + 1, board_w, board_h)
        elif key == ord(' '):
            # Rotate piece
            rotated = rotate_piece(current_piece)
            if can_place(board, rotated, current_x, current_y, board_w, board_h):
                current_piece = rotated
        
        # Draw everything
        draw_board(board_win, board, board_h, board_w)
        draw_info(info_win, score, level, lines_cleared, next_piece, board_h)
        
        board_win.refresh()
        info_win.refresh()
    
    # Game over
    if game_over_flag:
        board_win.clear()
        board_win.attron(curses.color_pair(2) | curses.A_BOLD)
        board_win.addstr(board_h // 2 - 1, board_w // 2 - 5, "GAME OVER!")
        board_win.addstr(board_h // 2, board_w // 2 - 8, f"Score: {score}")
        board_win.attroff(curses.color_pair(2) | curses.A_BOLD)
        board_win.refresh()
        time.sleep(2)
    
    # Wait for user to press a key
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def new_piece(board, board_w, board_h):
    """Create a new piece at the top of the board."""
    global current_piece, current_x, current_y, next_piece
    
    if next_piece is None:
        next_piece = random.randint(0, len(SHAPES) - 1)
    
    current_piece = next_piece
    next_piece = random.randint(0, len(SHAPES) - 1)
    
    shape = SHAPES[current_piece]
    current_x = (board_w - len(shape[0])) // 2
    current_y = 0
    
    # Check if piece can be placed
    if not can_place(board, shape, current_x, current_y, board_w, board_h):
        return False
    
    return True


def can_place(board, shape, x, y, board_w, board_h):
    """Check if a piece can be placed at the given position."""
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if (x + j < 0 or x + j >= board_w or
                    y + i >= board_h or
                    (y + i >= 0 and board[y + i][x + j])):
                    return False
    return True


def move_piece(board, shape, old_x, old_y, new_x, new_y, board_w, board_h):
    """Move the current piece to a new position."""
    global current_x, current_y
    
    if can_place(board, shape, new_x, new_y, board_w, board_h):
        current_x, current_y = new_x, new_y
        return True
    return False


def lock_piece(board, shape, x, y):
    """Lock the current piece in place on the board."""
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and y + i >= 0:
                board[y + i][x + j] = shape


def rotate_piece(shape):
    """Rotate a piece 90 degrees clockwise."""
    # Transpose and reverse each row
    return [list(row) for row in zip(*shape[::-1])]


def check_lines(board, board_h, board_w):
    """Check for and clear completed lines."""
    lines_cleared = 0
    for i in range(board_h):
        if all(board[i]):
            lines_cleared += 1
            # Move all lines above down
            for j in range(i, 0, -1):
                board[j] = board[j - 1][:]
            board[0] = [0 for _ in range(board_w)]
    return lines_cleared


def calculate_score(lines, level):
    """Calculate score based on lines cleared and level."""
    if lines == 0:
        return 0
    elif lines == 1:
        return 100 * level
    elif lines == 2:
        return 300 * level
    elif lines == 3:
        return 500 * level
    else:  # Tetris (4 lines)
        return 800 * level


def draw_board(win, board, board_h, board_w):
    """Draw the game board."""
    win.erase()
    win.attron(curses.color_pair(8))
    win.border()
    win.attroff(curses.color_pair(8))
    
    for y in range(board_h):
        for x in range(board_w):
            if board[y][x]:
                # Get the shape index from the board
                shape_idx = 0
                for i, shape in enumerate(SHAPES):
                    if board[y][x] == shape:
                        shape_idx = i
                        break
                
                win.attron(curses.color_pair(shape_idx + 1))
                try:
                    win.addch(y, x, curses.ACS_CKBOARD)
                except curses.error:
                    pass
                win.attroff(curses.color_pair(shape_idx + 1))
    
    # Draw current piece
    if current_piece is not None:
        shape = SHAPES[current_piece]
        win.attron(curses.color_pair(current_piece + 1))
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    try:
                        win.addch(current_y + i, current_x + j, curses.ACS_CKBOARD)
                    except curses.error:
                        pass
        win.attroff(curses.color_pair(current_piece + 1))


def draw_info(win, score, level, lines, next_piece_idx, board_h):
    """Draw the info panel."""
    win.erase()
    win.attron(curses.color_pair(9))
    win.addstr(0, 0, "TETRIS")
    win.addstr(2, 0, f"Score: {score}")
    win.addstr(4, 0, f"Level: {level}")
    win.addstr(6, 0, f"Lines: {lines}")
    win.addstr(8, 0, "Next:")
    
    # Draw next piece
    if next_piece_idx is not None:
        shape = SHAPES[next_piece_idx]
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    try:
                        win.addch(10 + i, 2 + j, curses.ACS_CKBOARD)
                    except curses.error:
                        pass
    
    win.addstr(14, 0, "Controls:")
    win.addstr(15, 0, "Arrows - Move")
    win.addstr(16, 0, "Space - Rotate")
    win.addstr(17, 0, "q - Quit")
    win.attroff(curses.color_pair(9))


# Global variables for the current piece
current_piece = None
current_x = 0
current_y = 0
next_piece = None


if __name__ == "__main__":
    main()
