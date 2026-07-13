# Terminal Games Collection
# A set of classic games that run in the Linux terminal

__version__ = "2.0.0"
__author__ = "Terminal Games Collection"

GAMES = {
    # Original fully-featured games
    "snake": "Snake Game - Use arrow keys to control the snake",
    "tetris": "Tetris - Classic block puzzle game",
    "pong": "Pong - Classic arcade game",
    "hangman": "Hangman - Word guessing game",
    "tic_tac_toe": "Tic Tac Toe - 2-player game",
    "game2048": "2048 - Number puzzle game",
    "minesweeper": "Minesweeper - Mine-hunting puzzle",
    "sudoku": "Sudoku - Number logic puzzle",
    "battleship": "Battleship - Naval combat game",
    "connect4": "Connect 4 - Disc-dropping game",
    "memory": "Memory Card Game - Match pairs",
    "quiz": "Quiz Game - General knowledge",
    "solitaire": "Solitaire - Klondike card game",
    
    # Card Games
    "blackjack": "Blackjack - Card game against the dealer",
    "poker": "Video Poker - 5-card draw poker",
    "war": "War - Simple card game",
    "go_fish": "Go Fish - Card matching game",
    "old_maid": "Old Maid - Card matching game",
    "crazy_eights": "Crazy Eights - Card shedding game",
    "baccarat": "Baccarat - Card comparison game",
    "bridge": "Bridge - Trick-taking card game",
    "canasta": "Canasta - Card melding game",
    "gin_rummy": "Gin Rummy - Card matching game",
    "hearts": "Hearts - Trick-taking card game",
    "spades": "Spades - Trick-taking card game",
    "euchre": "Euchre - Trick-taking card game",
    "pinochle": "Pinochle - Card melding game",
    "cribbage": "Cribbage - Card counting game",
    "uno": "Uno - Card shedding game",
    "skip_bo": "Skip-Bo - Card sequencing game",
    "phase_10": "Phase 10 - Card rummy game",
    "rummy": "Rummy - Card melding game",
    "solitaire_spider": "Spider Solitaire - Card game",
    "solitaire_free_cell": "FreeCell Solitaire - Card game",
    "solitaire_pyramid": "Pyramid Solitaire - Card game",
    "solitaire_tri_peaks": "TriPeaks Solitaire - Card game",
    "solitaire_golf": "Golf Solitaire - Card game",
    "mahjong": "Mahjong - Tile matching game",
    "dominoes": "Dominoes - Tile matching game",
    
    # Word Games
    "anagrams": "Anagrams - Word rearrangement game",
    "boggle": "Boggle - Word search in grid",
    "crossword": "Crossword Puzzle - Fill in the grid",
    "word_search": "Word Search - Find words in grid",
    "jumble": "Jumble - Unscramble words",
    "scrabble": "Scrabble - Word building game",
    "mad_libs": "Mad Libs - Fill-in-the-blank stories",
    
    # Puzzle Games
    "mastermind": "Mastermind - Code breaking game",
    "simon": "Simon - Memory sequence game",
    "lights_out": "Lights Out - Puzzle game",
    "peg_solitaire": "Peg Solitaire - Board puzzle",
    "tower_of_hanoi": "Tower of Hanoi - Disk puzzle",
    "fifteen_puzzle": "15 Puzzle - Sliding tile puzzle",
    "jigsaw": "Jigsaw Puzzle - Piece assembly",
    "maze": "Maze Game - Find the exit",
    "labyrinth": "Labyrinth - Maze navigation",
    
    # Dice and Casino Games
    "dice_roller": "Dice Roller - Roll various dice",
    "coin_flip": "Coin Flip - Heads or tails",
    "high_low": "High Low - Card guessing game",
    "number_guess": "Number Guess - Guess the number",
    "rock_paper_scissors": "Rock Paper Scissors - Hand game",
    "slots": "Slots - Casino slot machine",
    "roulette": "Roulette - Casino wheel game",
    "yahtzee": "Yahtzee - Dice scoring game",
    
    # Board Games
    "backgammon": "Backgammon - Board game",
    "checkers": "Checkers - Board game",
    "chess": "Chess - Strategy board game",
    "chinese_checkers": "Chinese Checkers - Board game",
    "go": "Go - Strategy board game",
    "shogi": "Shogi - Japanese chess",
    "xiangqi": "Xiangqi - Chinese chess",
    "snakes_and_ladders": "Snakes and Ladders - Board game",
    "monopoly": "Monopoly - Property trading game",
    "risk": "Risk - World conquest game",
    "clue": "Clue - Mystery deduction game",
    "battleship_advanced": "Advanced Battleship - Naval combat",
    "connect_five": "Connect Five - Disc-dropping game",
    "gomoku": "Gomoku - Five in a row",
    "reversi": "Reversi - Disc flipping game",
    
    # Arcade Classics
    "arcade_breakout": "Breakout - Brick breaking game",
    "arcade_pacman": "Pac-Man - Maze chase game",
    "arcade_space_invaders": "Space Invaders - Shooter game",
    "arcade_asteroids": "Asteroids - Space shooter",
    "arcade_centipede": "Centipede - Bug shooter",
    "arcade_frogger": "Frogger - Road crossing game",
    "arcade_donkey_kong": "Donkey Kong - Platform game",
    "arcade_galaga": "Galaga - Space shooter",
    "arcade_defender": "Defender - Space shooter",
    "arcade_battlezone": "Battlezone - Tank combat",
    "arcade_tempest": "Tempest - Space shooter",
    "arcade_pole_position": "Pole Position - Racing game",
    "arcade_dig_dug": "Dig Dug - Tunnel digging game",
    "arcade_qbert": "Q*bert - Pyramid jumping game",
    "arcade_galaxian": "Galaxian - Space shooter",
    "arcade_1942": "1942 - Air combat game",
    "arcade_1943": "1943 - Air combat game",
    "arcade_rampage": "Rampage - Monster destruction",
    "arcade_gauntlet": "Gauntlet - Dungeon crawler",
    "arcade_double_dragon": "Double Dragon - Fighting game",
    "arcade_teenage_mutant_ninja_turtles": "TMNT - Beat 'em up game",
    "arcade_street_fighter": "Street Fighter - Fighting game",
    "arcade_mortal_kombat": "Mortal Kombat - Fighting game",
    "arcade_tekken": "Tekken - Fighting game",
    "arcade_soul_calibur": "Soul Calibur - Fighting game",
    "arcade_king_of_fighters": "King of Fighters - Fighting game",
    "arcade_metal_slug": "Metal Slug - Run and gun",
    "arcade_contra": "Contra - Run and gun",
    "arcade_mega_man": "Mega Man - Platform shooter",
    "arcade_castlevania": "Castlevania - Platform adventure",
    "arcade_zelda": "Zelda - Adventure game",
    "arcade_mario": "Mario - Platform game",
    "arcade_sonic": "Sonic - Platform game",
    
    # RPG Games
    "arcade_final_fantasy": "Final Fantasy - RPG",
    "arcade_dragon_quest": "Dragon Quest - RPG",
    "arcade_pokemon": "Pokemon - Monster collecting RPG",
    "arcade_chrono_trigger": "Chrono Trigger - RPG",
    "arcade_earthbound": "EarthBound - RPG",
    "arcade_secret_of_mana": "Secret of Mana - Action RPG",
    "arcade_ff_tactics": "Final Fantasy Tactics - Strategy RPG",
    "arcade_fire_emblem": "Fire Emblem - Tactical RPG",
    
    # Strategy Games
    "arcade_advance_wars": "Advance Wars - Turn-based strategy",
    "arcade_civilization": "Civilization - Empire building",
    "arcade_xcom": "XCOM - Tactical strategy",
    "arcade_heroes_of_might_and_magic": "Heroes of Might and Magic - Strategy",
    "arcade_total_war": "Total War - Grand strategy",
    "arcade_crusader_kings": "Crusader Kings - Dynasty simulator",
    "arcade_stellaris": "Stellaris - Space strategy",
    "arcade_hearts_of_iron": "Hearts of Iron - WW2 strategy",
    "arcade_europa_universalis": "Europa Universalis - Historical strategy",
    "arcade_victoria": "Victoria - Economic strategy",
    "arcade_ck2": "Crusader Kings 2 - Medieval strategy",
    "arcade_hoi4": "Hearts of Iron 4 - WW2 grand strategy",
    
    # Simulation Games
    "arcade_starbound": "Starbound - Space adventure",
    "arcade_terraria": "Terraria - Sandbox adventure",
    "arcade_minecraft": "Minecraft - Sandbox building",
    "arcade_stardew_valley": "Stardew Valley - Farming simulation",
    "arcade_animal_crossing": "Animal Crossing - Life simulation",
    "arcade_sims": "The Sims - Life simulation",
    "arcade_rollercoaster_tycoon": "RollerCoaster Tycoon - Theme park sim",
    "arcade_zoo_tycoon": "Zoo Tycoon - Zoo management",
    "arcade_railroad_tycoon": "Railroad Tycoon - Train management",
    "arcade_city_builder": "City Builder - Urban planning",
    "arcade_farm_simulator": "Farm Simulator - Agriculture simulation",
    "arcade_flight_simulator": "Flight Simulator - Aviation simulation",
    
    # Racing Games
    "arcade_racing": "Racing Game - Car racing",
    "arcade_need_for_speed": "Need for Speed - Street racing",
    "arcade_gran_turismo": "Gran Turismo - Racing simulation",
    "arcade_mario_kart": "Mario Kart - Kart racing",
    "arcade_f_zero": "F-Zero - Futuristic racing",
    
    # Text Adventure
    "text_adventure": "Text Adventure - Interactive fiction",
    
    # Launcher
    "launcher": "Game Launcher - Browse and launch games",
}

def list_games():
    """List all available games."""
    print("\n" + "=" * 70)
    print("TERMINAL GAMES COLLECTION".center(70))
    print("=" * 70)
    print("\nAvailable Games:\n")
    for i, (name, description) in enumerate(GAMES.items(), 1):
        print(f"{i:3d}. {name:30s} - {description}")
    print(f"\n{len(GAMES)+1:3d}. exit              - Exit the game launcher")
    print("=" * 70)

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
