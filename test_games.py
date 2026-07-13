#!/usr/bin/env python3
"""
Test script to verify all games can be imported and have a main function
"""

import importlib
import sys
import os


def test_games():
    """Test that all games can be imported and have a main function."""
    games_dir = os.path.join(os.path.dirname(__file__), 'games')
    sys.path.insert(0, games_dir)
    
    # List of all game modules
    game_modules = [
        'snake', 'tetris', 'pong', 'hangman', 'tic_tac_toe',
        'game2048', 'minesweeper', 'sudoku', 'battleship',
        'connect4', 'memory', 'quiz', 'solitaire', 'launcher'
    ]
    
    print("Testing game modules...")
    print("=" * 50)
    
    all_passed = True
    
    for game_name in game_modules:
        try:
            module = importlib.import_module(f"games.{game_name}")
            if hasattr(module, 'main'):
                print(f"✓ {game_name:15s} - main() function found")
            else:
                print(f"✗ {game_name:15s} - No main() function")
                all_passed = False
        except ImportError as e:
            print(f"✗ {game_name:15s} - Import error: {e}")
            all_passed = False
        except Exception as e:
            print(f"✗ {game_name:15s} - Error: {e}")
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed! ✗")
        return 1


if __name__ == "__main__":
    sys.exit(test_games())
