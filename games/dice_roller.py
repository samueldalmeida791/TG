#!/usr/bin/env python3
"""
Dice Roller
Roll various types of dice.
"""

import random
import time


def main():
    """Main function to run the dice roller."""
    print("\n" + "=" * 50)
    print("DICE ROLLER".center(50))
    print("=" * 50)
    
    while True:
        print("\nSelect dice type:")
        print("1. Standard die (d6)")
        print("2. Two dice (2d6)")
        print("3. d4")
        print("4. d8")
        print("5. d10")
        print("6. d12")
        print("7. d20")
        print("8. d100")
        print("9. Custom dice")
        print("0. Exit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '0':
            print("Goodbye!")
            break
        elif choice == '1':
            roll = random.randint(1, 6)
            print(f"\nYou rolled: {roll}")
        elif choice == '2':
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            total = roll1 + roll2
            print(f"\nYou rolled: {roll1} + {roll2} = {total}")
        elif choice == '3':
            roll = random.randint(1, 4)
            print(f"\nYou rolled: {roll}")
        elif choice == '4':
            roll = random.randint(1, 8)
            print(f"\nYou rolled: {roll}")
        elif choice == '5':
            roll = random.randint(1, 10)
            print(f"\nYou rolled: {roll}")
        elif choice == '6':
            roll = random.randint(1, 12)
            print(f"\nYou rolled: {roll}")
        elif choice == '7':
            roll = random.randint(1, 20)
            print(f"\nYou rolled: {roll}")
        elif choice == '8':
            roll = random.randint(1, 100)
            print(f"\nYou rolled: {roll}")
        elif choice == '9':
            try:
                num_dice = int(input("Number of dice: "))
                num_sides = int(input("Number of sides: "))
                if num_dice < 1 or num_sides < 2:
                    print("Invalid input. Must have at least 1 die with at least 2 sides.")
                    continue
                
                rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
                total = sum(rolls)
                print(f"\nYou rolled: {' + '.join(map(str, rolls))} = {total}")
            except ValueError:
                print("Please enter valid numbers.")
        else:
            print("Invalid choice.")
        
        time.sleep(1)


if __name__ == "__main__":
    main()
