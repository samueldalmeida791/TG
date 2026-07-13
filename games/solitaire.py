#!/usr/bin/env python3
"""
Solitaire (Klondike) Game for Terminal
Use arrow keys to navigate, Enter to select, 'd' to draw, 'q' to quit.
"""

import curses
import random
import time


# Card suits and ranks
SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def main():
    """Main function to run the solitaire game."""
    # Initialize curses
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.timeout(100)
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)    # Hearts, Diamonds
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)  # Clubs, Spades
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal text
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Selected
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Border
    
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
    
    if sh < 25 or sw < 80:
        stdscr.addstr(sh // 2, sw // 2 - 15, "Terminal too small! (80x25 min)")
        stdscr.refresh()
        time.sleep(2)
        return
    
    # Initialize game
    deck = create_deck()
    random.shuffle(deck)
    
    # Game state
    tableau = [[[] for _ in range(7)] for _ in range(7)]  # 7 piles
    foundation = [[], [], [], []]  # 4 foundations
    stock = []
    waste = []
    
    # Deal cards to tableau
    for i in range(7):
        for j in range(i, 7):
            card = deck.pop()
            tableau[j][i].append(card)
    
    # Remaining cards go to stock
    stock = deck
    
    # Selected card
    selected_pile = None
    selected_pile_type = None  # 'tableau', 'waste', 'foundation'
    selected_index = 0
    
    # Game loop
    while True:
        # Draw everything
        draw_game(stdscr, tableau, foundation, stock, waste, selected_pile, 
                 selected_pile_type, selected_index, sh, sw)
        
        # Get input
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        elif key == ord('d'):
            # Draw from stock
            if stock:
                card = stock.pop()
                waste.append(card)
            elif waste:
                # Recycle waste back to stock
                stock = waste[::-1]
                waste = []
        elif key == curses.KEY_UP:
            # Move selection up
            if selected_pile_type == 'tableau' and selected_pile is not None:
                if selected_index > 0:
                    selected_index -= 1
        elif key == curses.KEY_DOWN:
            # Move selection down
            if selected_pile_type == 'tableau' and selected_pile is not None:
                if selected_index < len(tableau[selected_pile]) - 1:
                    selected_index += 1
        elif key == curses.KEY_LEFT:
            # Move selection left
            if selected_pile_type == 'tableau':
                if selected_pile is None:
                    selected_pile = 0
                    selected_index = len(tableau[0]) - 1 if tableau[0] else 0
                elif selected_pile > 0:
                    selected_pile -= 1
                    selected_index = min(selected_index, len(tableau[selected_pile]) - 1)
                else:
                    selected_pile = None
                    selected_pile_type = 'waste'
                    selected_index = 0
            elif selected_pile_type == 'waste':
                selected_pile = 0
                selected_pile_type = 'tableau'
                selected_index = len(tableau[0]) - 1 if tableau[0] else 0
            elif selected_pile_type == 'foundation':
                if selected_pile > 0:
                    selected_pile -= 1
                else:
                    selected_pile = None
                    selected_pile_type = 'waste'
                    selected_index = 0
        elif key == curses.KEY_RIGHT:
            # Move selection right
            if selected_pile_type == 'tableau':
                if selected_pile is None:
                    selected_pile = 0
                    selected_pile_type = 'foundation'
                    selected_index = 0
                elif selected_pile < 6:
                    selected_pile += 1
                    selected_index = min(selected_index, len(tableau[selected_pile]) - 1)
                else:
                    selected_pile = 0
                    selected_pile_type = 'foundation'
                    selected_index = 0
            elif selected_pile_type == 'waste':
                selected_pile = 0
                selected_pile_type = 'tableau'
                selected_index = len(tableau[0]) - 1 if tableau[0] else 0
            elif selected_pile_type == 'foundation':
                if selected_pile < 3:
                    selected_pile += 1
                else:
                    selected_pile = None
                    selected_pile_type = 'waste'
                    selected_index = 0
        elif key == ord('\n'):
            # Select/deselect
            if selected_pile_type is None:
                selected_pile = 0
                selected_pile_type = 'tableau'
                selected_index = len(tableau[0]) - 1 if tableau[0] else 0
            else:
                selected_pile_type = None
                selected_pile = None
        elif key == ord(' '):
            # Try to move selected card
            if selected_pile_type == 'tableau' and selected_pile is not None:
                if tableau[selected_pile] and selected_index < len(tableau[selected_pile]):
                    # Try to move to foundation
                    card = tableau[selected_pile][selected_index]
                    for i in range(4):
                        if can_move_to_foundation(card, foundation[i]):
                            # Move the card and all cards below it
                            cards_to_move = tableau[selected_pile][selected_index:]
                            foundation[i].extend(cards_to_move)
                            tableau[selected_pile] = tableau[selected_pile][:selected_index]
                            selected_pile_type = None
                            break
                    else:
                        # Try to move to another tableau pile
                        for i in range(7):
                            if i != selected_pile and can_move_to_tableau(card, tableau[i]):
                                cards_to_move = tableau[selected_pile][selected_index:]
                                tableau[i].extend(cards_to_move)
                                tableau[selected_pile] = tableau[selected_pile][:selected_index]
                                selected_pile = i
                                selected_index = len(tableau[i]) - len(cards_to_move)
                                break
            elif selected_pile_type == 'waste' and waste:
                card = waste[-1]
                # Try to move to foundation
                for i in range(4):
                    if can_move_to_foundation(card, foundation[i]):
                        foundation[i].append(waste.pop())
                        selected_pile_type = None
                        break
                else:
                    # Try to move to tableau
                    for i in range(7):
                        if can_move_to_tableau(card, tableau[i]):
                            tableau[i].append(waste.pop())
                            selected_pile = i
                            selected_pile_type = 'tableau'
                            selected_index = len(tableau[i]) - 1
                            break
            elif selected_pile_type == 'foundation' and selected_pile is not None:
                if foundation[selected_pile]:
                    card = foundation[selected_pile][-1]
                    # Try to move to tableau
                    for i in range(7):
                        if can_move_to_tableau(card, tableau[i]):
                            tableau[i].append(foundation[selected_pile].pop())
                            selected_pile = i
                            selected_pile_type = 'tableau'
                            selected_index = len(tableau[i]) - 1
                            break
        
        # Check if game is won
        if all(len(foundation[i]) > 0 for i in range(4)):
            draw_game(stdscr, tableau, foundation, stock, waste, selected_pile,
                     selected_pile_type, selected_index, sh, sw)
            stdscr.addstr(sh - 3, sw // 2 - 10, "CONGRATULATIONS! You won!")
            stdscr.refresh()
            time.sleep(2)
            break
    
    # Wait for user to press a key
    stdscr.addstr(sh - 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def create_deck():
    """Create a standard deck of 52 cards."""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    return deck


def can_move_to_foundation(card, foundation_pile):
    """Check if a card can be moved to a foundation pile."""
    rank, suit = card
    
    if not foundation_pile:
        # Can start with Ace
        return rank == 'A'
    
    top_card = foundation_pile[-1]
    top_rank, top_suit = top_card
    
    # Must be same suit and next rank
    if suit != top_suit:
        return False
    
    rank_index = RANKS.index(rank)
    top_rank_index = RANKS.index(top_rank)
    
    return rank_index == top_rank_index + 1


def can_move_to_tableau(card, tableau_pile):
    """Check if a card can be moved to a tableau pile."""
    rank, suit = card
    
    if not tableau_pile:
        # Can start with King
        return rank == 'K'
    
    top_card = tableau_pile[-1]
    top_rank, top_suit = top_card
    
    # Must be opposite color and descending rank
    suit_color = 'red' if suit in ['♥', '♦'] else 'black'
    top_suit_color = 'red' if top_suit in ['♥', '♦'] else 'black'
    
    if suit_color == top_suit_color:
        return False
    
    rank_index = RANKS.index(rank)
    top_rank_index = RANKS.index(top_rank)
    
    return rank_index == top_rank_index - 1


def get_card_color(suit):
    """Get the color pair for a card suit."""
    if suit in ['♥', '♦']:
        return 1  # Red
    else:
        return 2  # Black


def draw_game(stdscr, tableau, foundation, stock, waste, selected_pile,
             selected_pile_type, selected_index, sh, sw):
    """Draw the game state."""
    stdscr.erase()
    
    # Draw title
    stdscr.attron(curses.color_pair(3) | curses.A_BOLD)
    stdscr.addstr(0, sw // 2 - 10, "SOLITAIRE (Klondike)")
    stdscr.attroff(curses.color_pair(3) | curses.A_BOLD)
    
    # Draw instructions
    stdscr.addstr(1, 0, "Arrows: Navigate | Enter: Select | D: Draw | Space: Move | Q: Quit")
    
    # Draw stock and waste
    start_y = 3
    start_x = 5
    
    # Stock
    stdscr.addstr(start_y, start_x, "Stock:")
    if stock:
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(start_y + 1, start_x, "[XX]")
        stdscr.attroff(curses.color_pair(3))
    else:
        stdscr.addstr(start_y + 1, start_x, "[  ]")
    
    # Waste
    stdscr.addstr(start_y, start_x + 15, "Waste:")
    if waste:
        card = waste[-1]
        color = get_card_color(card[1])
        stdscr.attron(curses.color_pair(color))
        stdscr.addstr(start_y + 1, start_x + 15, f"[{card[0]}{card[1]}]")
        stdscr.attroff(curses.color_pair(color))
    else:
        stdscr.addstr(start_y + 1, start_x + 15, "[  ]")
    
    # Draw foundation
    foundation_start_x = start_x + 30
    stdscr.addstr(start_y, foundation_start_x, "Foundation:")
    for i in range(4):
        x = foundation_start_x + i * 8
        if foundation[i]:
            card = foundation[i][-1]
            color = get_card_color(card[1])
            stdscr.attron(curses.color_pair(color))
            stdscr.addstr(start_y + 1, x, f"[{card[0]}{card[1]}]")
            stdscr.attroff(curses.color_pair(color))
        else:
            stdscr.addstr(start_y + 1, x, "[  ]")
    
    # Draw tableau
    tableau_start_y = start_y + 3
    tableau_start_x = start_x
    
    stdscr.addstr(tableau_start_y - 1, tableau_start_x, "Tableau:")
    
    for pile_idx in range(7):
        x = tableau_start_x + pile_idx * 8
        pile = tableau[pile_idx]
        
        # Draw pile index
        stdscr.addstr(tableau_start_y, x, f"{pile_idx + 1}:")
        
        # Draw cards in pile
        for card_idx, card in enumerate(pile):
            y = tableau_start_y + 1 + card_idx
            rank, suit = card
            color = get_card_color(suit)
            
            # Check if this is the selected card
            is_selected = (selected_pile_type == 'tableau' and 
                          selected_pile == pile_idx and selected_index == card_idx)
            
            if is_selected:
                stdscr.attron(curses.color_pair(4) | curses.A_REVERSE)
            else:
                stdscr.attron(curses.color_pair(color))
            
            # Only show rank and suit for top card, others are face down
            if card_idx == len(pile) - 1:
                stdscr.addstr(y, x, f"[{rank}{suit}]")
            else:
                stdscr.addstr(y, x, "[XX]")
            
            stdscr.attroff(curses.color_pair(4) | curses.A_REVERSE if is_selected else curses.color_pair(color))
    
    # Draw selection indicator for waste and foundation
    if selected_pile_type == 'waste':
        stdscr.attron(curses.color_pair(4) | curses.A_REVERSE)
        if waste:
            stdscr.addstr(start_y + 1, start_x + 15, f"[{waste[-1][0]}{waste[-1][1]}]")
        else:
            stdscr.addstr(start_y + 1, start_x + 15, "[  ]")
        stdscr.attroff(curses.color_pair(4) | curses.A_REVERSE)
    
    if selected_pile_type == 'foundation' and selected_pile is not None:
        x = foundation_start_x + selected_pile * 8
        stdscr.attron(curses.color_pair(4) | curses.A_REVERSE)
        if foundation[selected_pile]:
            card = foundation[selected_pile][-1]
            stdscr.addstr(start_y + 1, x, f"[{card[0]}{card[1]}]")
        else:
            stdscr.addstr(start_y + 1, x, "[  ]")
        stdscr.attroff(curses.color_pair(4) | curses.A_REVERSE)
    
    stdscr.refresh()


if __name__ == "__main__":
    main()
