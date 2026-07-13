# Terminal Games Collection

A collection of classic games that can be run in the Linux terminal. All games are written in Python and use the `curses` library for terminal-based graphics.

## Games Included

1. **Snake** - Classic snake game with arrow key controls
2. **Tetris** - The classic block puzzle game
3. **Pong** - Classic arcade paddle game
4. **Hangman** - Word guessing game
5. **Tic Tac Toe** - 2-player game of X's and O's
6. **2048** - Number puzzle game
7. **Minesweeper** - Mine-hunting puzzle game
8. **Sudoku** - Number logic puzzle
9. **Battleship** - Naval combat game (Player vs Computer or Computer vs Computer)
10. **Connect 4** - Disc-dropping game
11. **Memory** - Card matching game
12. **Quiz** - General knowledge quiz

## Requirements

- Python 3.x
- Linux terminal (or any terminal that supports curses)
- Terminal size: At least 80x24 (most games require larger terminals)

## Installation

1. Clone this repository or download the files
2. Make sure Python 3 is installed
3. Make the launcher script executable:
   ```bash
   chmod +x play_games.sh
   ```

## Running the Games

### Method 1: Using the Launcher

Run the launcher script to see a menu of all available games:
```bash
./play_games.sh
```

Or use Python directly:
```bash
python3 -m games.launcher
```

### Method 2: Running Individual Games

You can run any game directly using Python:
```bash
python3 games/snake.py
python3 games/tetris.py
python3 games/pong.py
# etc.
```

## Game Controls

### Snake
- Arrow keys: Move snake
- q: Quit

### Tetris
- Arrow keys: Move piece
- Space: Rotate piece
- q: Quit

### Pong
- W/S: Move left paddle up/down
- I/K: Move right paddle up/down
- q: Quit

### Hangman
- Type letters to guess
- Enter 'quit' to exit

### Tic Tac Toe
- Enter row and column numbers (1-3) to place your mark
- Enter 'quit' to exit

### 2048
- Arrow keys: Move tiles
- q: Quit

### Minesweeper
- Arrow keys: Move cursor
- Space: Reveal cell
- f: Flag cell
- q: Quit

### Sudoku
- Arrow keys: Move cursor
- 1-9: Enter number
- Space: Clear cell
- s: Solve (cheat)
- q: Quit

### Battleship
- Enter coordinates (e.g., "A5") to make guesses
- Enter 'quit' to exit

### Connect 4
- Enter column number (1-7) to drop disc
- Enter 'quit' to exit

### Memory
- Enter card positions (e.g., "A1") to reveal cards
- Match pairs to win

### Quiz
- Enter the number of your answer choice
- Test your knowledge!

## Adding New Games

To add a new game:

1. Create a new Python file in the `games/` directory
2. Implement the game with a `main()` function
3. Add the game to the `GAMES` dictionary in `games/__init__.py`
4. The game will automatically appear in the launcher menu

## Troubleshooting

### Terminal too small
Most games require a minimum terminal size. If you see "Terminal too small!" message, try:
- Maximizing your terminal window
- Using a larger terminal emulator
- Running the game in fullscreen mode

### Curses errors
If you get errors related to curses, make sure:
- You're running the game in a proper terminal (not an IDE's built-in terminal)
- Your terminal supports curses
- You have the necessary Python curses module installed

### Python not found
If you get "Python not found" errors:
- Install Python 3: `sudo apt install python3` (on Debian/Ubuntu)
- Or use your distribution's package manager

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Contributing

Feel free to contribute new games or improvements to existing ones. Pull requests are welcome!

## Author

Terminal Games Collection - A collection of classic terminal games
