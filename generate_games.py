#!/usr/bin/env python3
"""
Script to generate multiple simple terminal games
"""

import os


# Simple text-based games that don't require curses
SIMPLE_GAMES = {
    "coin_flip": {
        "description": "Flip a coin - heads or tails",
        "code": '''#!/usr/bin/env python3
"""Coin Flip Game - Flip a coin and guess the outcome."""

import random
import time


def main():
    print("\\n" + "=" * 50)
    print("COIN FLIP".center(50))
    print("=" * 50)
    
    while True:
        print("\\n1. Flip coin")
        print("2. Quit")
        
        choice = input("\\nYour choice: ").strip()
        
        if choice == '2':
            print("Goodbye!")
            break
        elif choice == '1':
            guess = input("\\nHeads or Tails? (h/t): ").strip().lower()
            if guess not in ['h', 't']:
                print("Invalid choice. Please enter 'h' or 't'.")
                continue
            
            print("\\nFlipping...")
            time.sleep(1)
            
            result = random.choice(['heads', 'tails'])
            print(f"It's {result}!")
            
            if (guess == 'h' and result == 'heads') or (guess == 't' and result == 'tails'):
                print("You win!")
            else:
                print("You lose!")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
'''
    },
    
    "mad_libs": {
        "description": "Fill in the blanks to create funny stories",
        "code": '''#!/usr/bin/env python3
"""Mad Libs - Fill in the blanks to create funny stories."""

import random


STORIES = [
    {
        "title": "The Adventure",
        "template": "One day, {name} went to {place} to find {object}. "
                   "Along the way, they met a {adjective} {animal} who "
                   "said, '{exclamation}'! Finally, they {verb} all the way home.",
        "prompts": [
            ("name", "a person's name"),
            ("place", "a place"),
            ("object", "an object"),
            ("adjective", "an adjective"),
            ("animal", "an animal"),
            ("exclamation", "an exclamation"),
            ("verb", "a verb ending in -ed")
        ]
    },
    {
        "title": "The Party",
        "template": "There was a {adjective} party at {name}'s house. "
                   "Everyone brought {food} and {drink}. "
                   "The music was {adjective} and loud! "
                   "At midnight, {name} {verb} on the table and shouted '{exclamation}'!",
        "prompts": [
            ("adjective", "an adjective"),
            ("name", "a person's name"),
            ("food", "a food"),
            ("drink", "a drink"),
            ("adjective", "an adjective"),
            ("name", "a person's name"),
            ("verb", "a verb ending in -ed"),
            ("exclamation", "an exclamation")
        ]
    },
    {
        "title": "The Monster",
        "template": "Beware the {adjective} {monster} that lives in {place}! "
                   "It has {number} {body_part} and loves to {verb}. "
                   "If you see it, {action} and yell '{exclamation}'!",
        "prompts": [
            ("adjective", "an adjective"),
            ("monster", "a monster"),
            ("place", "a place"),
            ("number", "a number"),
            ("body_part", "a body part"),
            ("verb", "a verb"),
            ("action", "an action"),
            ("exclamation", "an exclamation")
        ]
    }
]


def main():
    print("\\n" + "=" * 50)
    print("MAD LIBS".center(50))
    print("=" * 50)
    
    while True:
        print("\\nSelect a story:")
        for i, story in enumerate(STORIES, 1):
            print(f"{i}. {story['title']}")
        print("0. Random")
        print("9. Quit")
        
        choice = input("\\nYour choice: ").strip()
        
        if choice == '9':
            print("Goodbye!")
            break
        
        try:
            if choice == '0':
                story = random.choice(STORIES)
            else:
                story = STORIES[int(choice) - 1]
            
            print(f"\\n{story['title']}")
            print("-" * len(story['title']))
            
            # Collect words
            words = {}
            for var, prompt in story['prompts']:
                words[var] = input(f"Enter {prompt}: ").strip()
            
            # Generate and display story
            print("\\n" + "=" * 50)
            print("YOUR STORY:")
            print("=" * 50)
            print(story['template'].format(**words))
            print("=" * 50)
        except (ValueError, IndexError, KeyError):
            print("Invalid choice.")


if __name__ == "__main__":
    main()
'''
    },
    
    "trivia": {
        "description": "Answer trivia questions",
        "code": '''#!/usr/bin/env python3
"""Trivia Game - Answer general knowledge questions."""

import random


QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "category": "Geography"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci",
        "category": "Art"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter",
        "category": "Science"
    },
    {
        "question": "In which year did World War II end?",
        "answer": "1945",
        "category": "History"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "Au",
        "category": "Chemistry"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "answer": "William Shakespeare",
        "category": "Literature"
    },
    {
        "question": "What is the tallest mammal?",
        "answer": "Giraffe",
        "category": "Animals"
    },
    {
        "question": "Which country is home to the kangaroo?",
        "answer": "Australia",
        "category": "Geography"
    },
    {
        "question": "What is the hardest natural substance?",
        "answer": "Diamond",
        "category": "Science"
    },
    {
        "question": "Who was the first man to walk on the moon?",
        "answer": "Neil Armstrong",
        "category": "History"
    }
]


def main():
    print("\\n" + "=" * 50)
    print("TRIVIA GAME".center(50))
    print("=" * 50)
    
    score = 0
    total = 0
    
    while True:
        if total >= len(QUESTIONS):
            print(f"\\nGame over! Your score: {score}/{total}")
            print(f"Percentage: {score/total*100:.1f}%")
            break
        
        # Select a random question
        question = random.choice(QUESTIONS)
        
        print(f"\\nCategory: {question['category']}")
        print(f"Question {total + 1}: {question['question']}")
        
        answer = input("Your answer: ").strip()
        
        if answer.lower() == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")
        
        total += 1
        
        print(f"\\nScore: {score}/{total}")
        
        # Ask to continue
        cont = input("\\nContinue? (y/n): ").strip().lower()
        if cont != 'y':
            print(f"\\nFinal score: {score}/{total}")
            print(f"Percentage: {score/total*100:.1f}%")
            break


if __name__ == "__main__":
    main()
'''
    }
}


def create_game_file(game_name, description, code):
    """Create a game file."""
    filename = f"games/{game_name}.py"
    
    # Add the main function wrapper
    full_code = f'''#!/usr/bin/env python3
"""
{description}
"""

{code}

if __name__ == "__main__":
    main()
'''
    
    with open(filename, 'w') as f:
        f.write(full_code)
    
    print(f"Created: {filename}")


def main():
    """Generate all the simple games."""
    # Create games directory if it doesn't exist
    os.makedirs('games', exist_ok=True)
    
    # Generate simple games
    for game_name, game_data in SIMPLE_GAMES.items():
        create_game_file(game_name, game_data['description'], game_data['code'])
    
    print("\nAll games generated successfully!")


if __name__ == "__main__":
    main()
