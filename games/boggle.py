#!/usr/bin/env python3
"""Boggle - Word Game - Find words in a grid of letters."""

import random
import time


# Dictionary of valid words (3+ letters)
DICTIONARY = {
    'cat', 'dog', 'bat', 'rat', 'hat', 'mat', 'sat', 'pat', 'fat', 'vat',
    'and', 'the', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can',
    'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his',
    'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy',
    'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use', 'apple', 'apply',
    'bake', 'baker', 'ball', 'band', 'bank', 'bar', 'bare', 'bark', 'base',
    'bear', 'beat', 'bed', 'bee', 'beer', 'bell', 'bend', 'bet', 'bite',
    'black', 'blue', 'boat', 'body', 'bone', 'book', 'boot', 'born', 'both',
    'bowl', 'box', 'bread', 'break', 'bright', 'brown', 'brush', 'burn',
    'call', 'calm', 'came', 'camp', 'can', 'card', 'care', 'case', 'cast',
    'cat', 'catch', 'chain', 'chair', 'chalk', 'chance', 'change', 'chart',
    'chase', 'cheap', 'check', 'cheek', 'cheer', 'chest', 'chief', 'child',
    'chill', 'chip', 'chose', 'clean', 'clear', 'clever', 'climb', 'clock',
    'close', 'cloud', 'coach', 'coast', 'coat', 'code', 'coffee', 'cold',
    'color', 'come', 'common', 'company', 'complete', 'complex', 'concept',
    'concern', 'condition', 'conference', 'confidence', 'conflict', 'congress',
    'connect', 'consist', 'constant', 'contact', 'contain', 'content',
    'dance', 'danger', 'dare', 'dark', 'data', 'date', 'daughter', 'day',
    'dead', 'deal', 'dear', 'death', 'debate', 'debt', 'decade', 'decide',
    'deck', 'declare', 'decorate', 'decrease', 'deep', 'defeat', 'defend',
    'define', 'degree', 'delay', 'deliver', 'demand', 'depend', 'describe',
    'desert', 'design', 'desire', 'detail', 'detect', 'develop', 'device',
}


def create_board(size=4):
    """Create a Boggle board."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.choice(letters))
        board.append(row)
    return board


def print_board(board):
    """Print the Boggle board."""
    for row in board:
        print(' '.join(row))


def find_words(board, size=4):
    """Find all valid words on the board."""
    words = set()
    
    def dfs(i, j, path, visited):
        if i < 0 or i >= size or j < 0 or j >= size or visited[i][j]:
            return
        
        path.append(board[i][j])
        visited[i][j] = True
        
        word = ''.join(path)
        if len(word) >= 3 and word in DICTIONARY:
            words.add(word)
        
        # Explore neighbors
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                dfs(i + di, j + dj, path, visited)
        
        path.pop()
        visited[i][j] = False
    
    for i in range(size):
        for j in range(size):
            dfs(i, j, [], [[False for _ in range(size)] for _ in range(size)])
    
    return sorted(words)


def main():
    """Main function to run the Boggle game."""
    print("\n" + "=" * 50)
    print("BOGGLE".center(50))
    print("=" * 50)
    print("\nFind words in the grid (3+ letters).")
    print("Words can be formed by adjacent letters (including diagonals).")
    print("Type 'quit' to exit.")
    
    board = create_board()
    all_words = find_words(board)
    
    print("\n" + "=" * 50)
    print_board(board)
    print("=" * 50)
    
    found_words = set()
    score = 0
    
    while True:
        word = input("\nEnter a word: ").strip().lower()
        
        if word == 'quit':
            print(f"\nGoodbye! Score: {score}")
            print(f"You found {len(found_words)}/{len(all_words)} words.")
            if len(found_words) < len(all_words):
                missing = [w for w in all_words if w not in found_words]
                print(f"\nWords you missed: {', '.join(missing[:10])}{'...' if len(missing) > 10 else ''}")
            break
        
        if len(word) < 3:
            print("Words must be at least 3 letters long.")
            continue
        
        if word in found_words:
            print("You already found that word.")
            continue
        
        if word in all_words:
            print(f"Good! '{word}' is valid.")
            found_words.add(word)
            score += len(word)
        else:
            print(f"'{word}' is not a valid word on this board.")
            score = max(0, score - 1)
        
        print(f"Score: {score} | Found: {len(found_words)}/{len(all_words)}")


if __name__ == "__main__":
    main()
