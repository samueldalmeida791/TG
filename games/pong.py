#!/usr/bin/env python3
"""
Pong Game for Terminal
Use 'w' and 's' for left paddle, 'i' and 'k' for right paddle. Press 'q' to quit.
"""

import curses
import time
import random


def main():
    """Main function to run the pong game."""
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(50)
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Paddles and ball
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Score
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Border
    
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
    if sh < 15 or sw < 40:
        stdscr.addstr(sh // 2, sw // 2 - 10, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return
    
    # Paddle dimensions
    paddle_h = 4
    paddle_w = 1
    
    # Initialize paddles
    left_paddle_y = sh // 2 - paddle_h // 2
    right_paddle_y = sh // 2 - paddle_h // 2
    
    # Initialize ball
    ball_x = sw // 2
    ball_y = sh // 2
    ball_dx = 1 if random.random() > 0.5 else -1
    ball_dy = 1 if random.random() > 0.5 else -1
    
    # Scores
    left_score = 0
    right_score = 0
    
    # Game loop
    while True:
        stdscr.erase()
        
        # Draw border
        stdscr.attron(curses.color_pair(3))
        stdscr.border()
        stdscr.attroff(curses.color_pair(3))
        
        # Draw paddles
        stdscr.attron(curses.color_pair(1))
        for i in range(paddle_h):
            try:
                stdscr.addch(left_paddle_y + i, 1, curses.ACS_CKBOARD)
                stdscr.addch(right_paddle_y + i, sw - 2, curses.ACS_CKBOARD)
            except curses.error:
                pass
        stdscr.attroff(curses.color_pair(1))
        
        # Draw ball
        stdscr.attron(curses.color_pair(1))
        try:
            stdscr.addch(ball_y, ball_x, curses.ACS_DIAMOND)
        except curses.error:
            pass
        stdscr.attroff(curses.color_pair(1))
        
        # Draw scores
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(0, sw // 2 - 5, f"{left_score} - {right_score}")
        stdscr.attroff(curses.color_pair(2))
        
        # Draw instructions
        stdscr.addstr(sh - 1, 0, "W/S - Left | I/K - Right | Q - Quit")
        
        stdscr.refresh()
        
        # Get input
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == ord('w') and left_paddle_y > 1:
            left_paddle_y -= 1
        elif key == ord('s') and left_paddle_y + paddle_h < sh - 1:
            left_paddle_y += 1
        elif key == ord('i') and right_paddle_y > 1:
            right_paddle_y -= 1
        elif key == ord('k') and right_paddle_y + paddle_h < sh - 1:
            right_paddle_y += 1
        
        # Move ball
        ball_x += ball_dx
        ball_y += ball_dy
        
        # Ball collision with top and bottom
        if ball_y <= 1 or ball_y >= sh - 2:
            ball_dy *= -1
        
        # Ball collision with paddles
        if ball_x <= 2 and left_paddle_y <= ball_y < left_paddle_y + paddle_h:
            ball_dx = 1
            # Add some randomness to the bounce
            ball_dy += random.randint(-1, 1)
        elif ball_x >= sw - 3 and right_paddle_y <= ball_y < right_paddle_y + paddle_h:
            ball_dx = -1
            ball_dy += random.randint(-1, 1)
        
        # Ball out of bounds (score)
        if ball_x <= 0:
            right_score += 1
            reset_ball(sw, sh)
            ball_x, ball_y, ball_dx, ball_dy = sw // 2, sh // 2, 1, 1
        elif ball_x >= sw - 1:
            left_score += 1
            reset_ball(sw, sh)
            ball_x, ball_y, ball_dx, ball_dy = sw // 2, sh // 2, -1, -1
        
        # Limit ball speed
        ball_dy = max(-1, min(1, ball_dy))
        
        # Small delay
        time.sleep(0.05)
    
    # Wait for user to press a key
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def reset_ball(sw, sh):
    """Reset ball position."""
    time.sleep(1)


if __name__ == "__main__":
    main()
