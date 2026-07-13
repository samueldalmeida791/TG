#!/usr/bin/env python3
"""
Terminal Games Launcher
A collection of games that can be run in the Linux terminal.
"""

import os
import sys
import subprocess


def main():
    """Main launcher function."""
    # Add the games directory to the path
    games_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, games_dir)
    
    # Import the games module
    from games import GAMES, list_games, run_game
    
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Show welcome message
    print("\n" + "=" * 60)
    print("TERMINAL GAMES COLLECTION".center(60))
    print("=" * 60)
    print("\nWelcome to the Terminal Games Collection!")
    print("Select a game to play or type 'exit' to quit.")
    
    # Main loop
    while True:
        list_games()
        
        try:
            choice = input("\nEnter game number or name: ").strip().lower()
            
            if choice == 'exit':
                print("\nGoodbye! Thanks for playing!")
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
            print("\n\nGoodbye! Thanks for playing!")
            break
        except EOFError:
            print("\n\nGoodbye! Thanks for playing!")
            break


if __name__ == "__main__":
    main()
