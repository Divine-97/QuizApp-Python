import random

quiz_data = [
    {"question": "Who is the most followed Celebrity on Instagram?",
     "answers": {"A": "Kylie Jenner",
                 "B": "Cristiano Ronaldo",
                 "C": "Kim Kardashian"},
     "correct_answer": "B"},
    {"question": "What is the largest Continent in size?",
     "answers": {"A": "Asia",
                 "B": "Europe",
                 "C": "Africa"},
     "correct_answer": "A"},
    {"question": "Which country is Westlife from?",
     "answers": {"A": "USA",
                 "B": "Australia",
                 "C": "Ireland"},
     "correct_answer": "C"},

    {"question": "How many Organs are in the human body",
     "answers": {"A": "88",
                 "B": "78",
                 "C": "12"},
     "correct_answer": "B"},
    {"question": "Who is the best F1 driver?",
     "answers": {"A": "Lewis Hamilton",
                 "B": "Max Verstappen",
                 "C": "Michael Schumacher"},
     "correct_answer": "A"},
    {"question": "What color pill does Neo swallow in The Matrix movie?",
     "answers": {"A": "Blue",
                 "B": "Green",
                 "C": "Red"},
     "correct_answer": "C"},
    {"question": "Which of these zodiac signs is not an earth sign?",
     "answers": {"A": "Taurus",
                 "B": "Scorpio",
                 "C": "Virgo"},
     "correct_answer": "B"},
    {"question": "Which country is the origin of the cocktail Mojito",
     "answers": {"A": "Cuba",
                 "B": "Spain",
                 "C": "Italy"},
     "correct_answer": "B"},
    {"question": "How many contries are there in the world?",
     "answers": {"A": "195",
                 "B": "201",
                 "C": "190"},
     "correct_answer": "A"},
    {"question": "How many infinity stones were there in Black Panther?",
     "answers": {"A": "8",
                 "B": "9",
                 "C": "6"},
     "correct_answer": "C"},
]



def start():
    """
    Run all program functions
    """
    print("\nWelcome to Quizzer")
    print("\nLet's test your Knowledge")
    
    name = input("Please type your name and hit the enter key:\n")

    while not name.strip():
        print("Please enter your name to begin the quiz\n")
        name = input("Please type your name and hit the enter key:\n")
    else:
        print(f"There are {num_of_questions} multiple choice questions.\n")
        print("Select your answer by typing 'a', 'b' or 'c'.\n")
        print("Good luck!\n")

    begin_quiz = True

    while begin_quiz:
        commence_quiz = input("Are you ready to begin? y/n\n")

        if commence_quiz.lower() == "y":
            print("Lets go\n")
            break
        elif commence_quiz.lower() == "n":
            print("Type 'y' when you are ready to begin\n")
        else:
            print("That is not a valid option\n")
    
        

