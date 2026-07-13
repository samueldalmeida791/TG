# Terminal Games Collection
# A set of classic games that run in the Linux terminal

__version__ = "1.0.0"
__author__ = "Terminal Games Collection"

GAMES = {
    "snake": "Snake Game - Use arrow keys to control the snake",
    "tetris": "Tetris - Classic block puzzle game",
    "pong": "Pong - Classic arcade game",
    "hangman": "Hangman - Word guessing game",
    "tic_tac_toe": "Tic Tac Toe - 2-player game",
    "2048": "2048 - Number puzzle game",
    "minesweeper": "Minesweeper - Mine-hunting puzzle",
    "sudoku": "Sudoku - Number logic puzzle",
    "battleship": "Battleship - Naval combat game",
    "connect4": "Connect 4 - Disc-dropping game",
    "memory": "Memory Card Game - Match pairs",
    "quiz": "Quiz Game - General knowledge",
    "solitaire": "Solitaire - Klondike card game",
}

def list_games():
    """List all available games."""
    print("\n" + "=" * 50)
    print("TERMINAL GAMES COLLECTION".center(50))
    print("=" * 50)
    print("\nAvailable Games:\n")
    for i, (name, description) in enumerate(GAMES.items(), 1):
        print(f"{i:2d}. {name:15s} - {description}")
    print(f"\n{len(GAMES)+1:2d}. exit              - Exit the game launcher")
    print("=" * 50)

def run_game(name):
    """Run a specific game by name."""
    import importlib
    try:
        module = importlib.import_module(f"games.{name}")
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"Game '{name}' doesn't have a main function")
    except ImportError:
        print(f"Game '{name}' not found")
    except Exception as e:
        print(f"Error running game '{name}': {e}")

def main():
    """Main game launcher."""
    import sys
    
    if len(sys.argv) > 1:
        game_name = sys.argv[1]
        run_game(game_name)
    else:
        # Interactive menu
        while True:
            list_games()
            try:
                choice = input("\nEnter game number or name: ").strip().lower()
                
                if choice == 'exit' or choice == str(len(GAMES) + 1):
                    print("Goodbye!")
                    break
                
                # Try as number first
                try:
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(GAMES):
                        game_name = list(GAMES.keys())[choice_num - 1]
                        run_game(game_name)
                        continue
                except ValueError:
                    pass
                
                # Try as name
                if choice in GAMES:
                    run_game(choice)
                else:
                    print(f"Unknown game: {choice}")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    main()
