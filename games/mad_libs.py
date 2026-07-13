#!/usr/bin/env python3
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
                   "The music was {adjective2} and loud! "
                   "At midnight, {name2} {verb} on the table and shouted '{exclamation}'!",
        "prompts": [
            ("adjective", "an adjective"),
            ("name", "a person's name"),
            ("food", "a food"),
            ("drink", "a drink"),
            ("adjective2", "an adjective"),
            ("name2", "a person's name"),
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
    print("\n" + "=" * 50)
    print("MAD LIBS".center(50))
    print("=" * 50)
    
    while True:
        print("\nSelect a story:")
        for i, story in enumerate(STORIES, 1):
            print(f"{i}. {story['title']}")
        print("0. Random")
        print("9. Quit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '9':
            print("Goodbye!")
            break
        
        try:
            if choice == '0':
                story = random.choice(STORIES)
            else:
                story = STORIES[int(choice) - 1]
            
            print(f"\n{story['title']}")
            print("-" * len(story['title']))
            
            # Collect words
            words = {}
            for var, prompt in story['prompts']:
                words[var] = input(f"Enter {prompt}: ").strip()
            
            # Generate and display story
            print("\n" + "=" * 50)
            print("YOUR STORY:")
            print("=" * 50)
            print(story['template'].format(**words))
            print("=" * 50)
        except (ValueError, IndexError, KeyError):
            print("Invalid choice.")


if __name__ == "__main__":
    main()
