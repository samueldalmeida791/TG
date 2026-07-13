#!/usr/bin/env python3
"""
Quiz Game for Terminal
Test your knowledge with various quiz categories.
"""

import random
import time
import sys


# Quiz questions and answers
QUIZ_CATEGORIES = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": 1,
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": 1,
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": 3,
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "answer": 2,
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Go", "Gd", "Au", "Ag"],
            "answer": 2,
        },
    ],
    "Science": [
        {
            "question": "What is the speed of light in a vacuum?",
            "options": ["299,792 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"],
            "answer": 0,
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["Helium", "Hydrogen", "Oxygen", "Carbon"],
            "answer": 1,
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Quartz"],
            "answer": 2,
        },
        {
            "question": "What is the pH value of pure water?",
            "options": ["0", "7", "14", "1"],
            "answer": 1,
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "answer": 2,
        },
    ],
    "History": [
        {
            "question": "In which year did World War II end?",
            "options": ["1944", "1945", "1946", "1947"],
            "answer": 1,
        },
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
            "answer": 1,
        },
        {
            "question": "The ancient city of Petra is located in which country?",
            "options": ["Egypt", "Israel", "Jordan", "Saudi Arabia"],
            "answer": 2,
        },
        {
            "question": "Which civilization built the pyramids at Giza?",
            "options": ["Greek", "Roman", "Egyptian", "Mayan"],
            "answer": 2,
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1905", "1912", "1918", "1923"],
            "answer": 1,
        },
    ],
    "Geography": [
        {
            "question": "What is the longest river in the world?",
            "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
            "answer": 1,
        },
        {
            "question": "Which country has the largest land area?",
            "options": ["China", "United States", "Russia", "Canada"],
            "answer": 2,
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
            "answer": 2,
        },
        {
            "question": "Which mountain range separates Europe from Asia?",
            "options": ["Alps", "Himalayas", "Ural Mountains", "Rocky Mountains"],
            "answer": 2,
        },
        {
            "question": "What is the largest desert in the world?",
            "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert"],
            "answer": 3,
        },
    ],
    "Programming": [
        {
            "question": "Which programming language was created first?",
            "options": ["Python", "C", "Java", "Fortran"],
            "answer": 3,
        },
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Machine Language", 
                       "Hyperlink and Text Markup Language", "Home Tool Markup Language"],
            "answer": 0,
        },
        {
            "question": "Which company developed the Python programming language?",
            "options": ["Microsoft", "Google", "Sun Microsystems", "None of the above"],
            "answer": 3,
        },
        {
            "question": "What is the most widely used operating system for servers?",
            "options": ["Windows", "macOS", "Linux", "FreeBSD"],
            "answer": 2,
        },
        {
            "question": "Which data structure uses LIFO (Last In, First Out)?",
            "options": ["Queue", "Stack", "Array", "Linked List"],
            "answer": 1,
        },
    ],
}


def main():
    """Main function to run the quiz game."""
    print("\n" + "=" * 50)
    print("QUIZ GAME".center(50))
    print("=" * 50)
    
    # Select category
    print("\nSelect a category:")
    for i, category in enumerate(QUIZ_CATEGORIES.keys(), 1):
        print(f"{i}. {category}")
    print(f"{len(QUIZ_CATEGORIES) + 1}. Random")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-{}): ".format(len(QUIZ_CATEGORIES) + 1))
            choice = int(choice)
            if 1 <= choice <= len(QUIZ_CATEGORIES) + 1:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")
    
    if choice == len(QUIZ_CATEGORIES) + 1:
        category = random.choice(list(QUIZ_CATEGORIES.keys()))
        questions = QUIZ_CATEGORIES[category]
    else:
        category = list(QUIZ_CATEGORIES.keys())[choice - 1]
        questions = QUIZ_CATEGORIES[category]
    
    print(f"\nYou selected: {category}")
    print(f"There are {len(questions)} questions.")
    
    # Select number of questions
    num_questions = min(len(questions), 10)
    try:
        num = input(f"\nHow many questions would you like? (1-{num_questions}): ").strip()
        num_questions = int(num)
        if num_questions < 1 or num_questions > len(questions):
            num_questions = len(questions)
    except ValueError:
        pass
    
    # Select questions
    selected_questions = random.sample(questions, num_questions)
    
    # Game state
    score = 0
    
    # Game loop
    for i, question_data in enumerate(selected_questions, 1):
        print("\n" + "=" * 50)
        print(f"Question {i}/{num_questions}".center(50))
        print("=" * 50)
        print(f"\n{question_data['question']}")
        
        # Display options
        for j, option in enumerate(question_data['options'], 1):
            print(f"{j}. {option}")
        
        # Get user answer
        while True:
            try:
                answer = input("\nYour answer (1-{}): ".format(len(question_data['options'])))
                answer = int(answer)
                if 1 <= answer <= len(question_data['options']):
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
        
        # Check answer
        if answer - 1 == question_data['answer']:
            print("\nCorrect!")
            score += 1
        else:
            print(f"\nWrong! The correct answer is: {question_data['options'][question_data['answer']]}")
        
        time.sleep(1)
    
    # Game over
    print("\n" + "=" * 50)
    print("QUIZ COMPLETE".center(50))
    print("=" * 50)
    print(f"\nYour score: {score}/{num_questions}")
    print(f"Percentage: {score / num_questions * 100:.1f}%")
    
    # Rate the player
    if score / num_questions >= 0.9:
        print("\nExcellent! You're a genius!")
    elif score / num_questions >= 0.7:
        print("\nGreat job! You know your stuff!")
    elif score / num_questions >= 0.5:
        print("\nGood effort! Keep learning!")
    else:
        print("\nKeep practicing! You'll get better!")


if __name__ == "__main__":
    main()
