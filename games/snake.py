#!/usr/bin/env python3
"""
Snake Game for Terminal
Use arrow keys to control the snake. Press 'q' to quit.
"""

import curses
import random
import time
import sys


def main():
    """Main function to run the snake game."""
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(100)
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Border
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Score
    
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
    
    # Create game window
    win_h, win_w = sh - 2, sw - 2
    if win_h < 10 or win_w < 20:
        stdscr.addstr(sh // 2, sw // 2 - 10, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return
    
    win = curses.newwin(win_h, win_w, 1, 1)
    win.keypad(True)
    win.timeout(100)
    
    # Initialize snake
    snake = [[win_h // 2, win_w // 2]]
    direction = curses.KEY_RIGHT
    
    # Initialize food
    food = [win_h // 2, win_w // 4]
    place_food(win, food, snake, win_h, win_w)
    
    # Score
    score = 0
    
    # Game loop
    while True:
        # Get next key
        key = win.getch()
        
        # Handle input
        if key == ord('q'):
            break
        elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            # Prevent 180-degree turns
            if (key == curses.KEY_UP and direction != curses.KEY_DOWN) or \
               (key == curses.KEY_DOWN and direction != curses.KEY_UP) or \
               (key == curses.KEY_LEFT and direction != curses.KEY_RIGHT) or \
               (key == curses.KEY_RIGHT and direction != curses.KEY_LEFT):
                direction = key
        
        # Move snake
        head = snake[0].copy()
        if direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1
        
        # Check for collisions
        if (head[0] < 0 or head[0] >= win_h or 
            head[1] < 0 or head[1] >= win_w or
            head in snake[1:]):
            game_over(win, score, win_h, win_w)
            break
        
        # Check for food
        if head == food:
            snake.insert(0, head)
            score += 10
            place_food(win, food, snake, win_h, win_w)
        else:
            snake.insert(0, head)
            snake.pop()
        
        # Draw everything
        win.erase()
        draw_border(win, win_h, win_w)
        draw_snake(win, snake)
        draw_food(win, food)
        draw_score(stdscr, score, sw)
        win.refresh()
        
        # Speed up as score increases
        if score > 0 and score % 100 == 0:
            win.timeout(max(50, 150 - score // 10))
    
    # Wait for user to press a key before exiting
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def place_food(win, food, snake, win_h, win_w):
    """Place food at a random position not occupied by the snake."""
    while True:
        food[0] = random.randint(0, win_h - 1)
        food[1] = random.randint(0, win_w - 1)
        if food not in snake:
            break


def draw_border(win, win_h, win_w):
    """Draw the game border."""
    win.attron(curses.color_pair(3))
    win.border()
    win.attroff(curses.color_pair(3))


def draw_snake(win, snake):
    """Draw the snake."""
    win.attron(curses.color_pair(1))
    for segment in snake:
        try:
            win.addch(segment[0], segment[1], curses.ACS_CKBOARD)
        except curses.error:
            pass
    win.attroff(curses.color_pair(1))


def draw_food(win, food):
    """Draw the food."""
    win.attron(curses.color_pair(2))
    try:
        win.addch(food[0], food[1], curses.ACS_DIAMOND)
    except curses.error:
        pass
    win.attroff(curses.color_pair(2))


def draw_score(stdscr, score, sw):
    """Draw the score at the top of the screen."""
    stdscr.attron(curses.color_pair(4))
    stdscr.addstr(0, 0, f"Score: {score}")
    stdscr.attroff(curses.color_pair(4))


def game_over(win, score, win_h, win_w):
    """Display game over message."""
    win.clear()
    win.attron(curses.color_pair(2) | curses.A_BOLD)
    win.addstr(win_h // 2 - 1, win_w // 2 - 5, "GAME OVER!")
    win.addstr(win_h // 2, win_w // 2 - 8, f"Final Score: {score}")
    win.addstr(win_h // 2 + 1, win_w // 2 - 10, "Press 'q' to quit")
    win.attroff(curses.color_pair(2) | curses.A_BOLD)
    win.refresh()
    time.sleep(1)


if __name__ == "__main__":
    main()
