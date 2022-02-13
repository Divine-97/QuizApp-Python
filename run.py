import colorama
import random
from colorama import Fore, Style
colorama.init(autoreset=True)

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

    {"question": "How many Organs are in the human body?",
     "answers": {"A": "88",
                 "B": "78",
                 "C": "12"},
     "correct_answer": "B"},
    {"question": "Which F1 driver has the most wins?",
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
    {"question": "Which country is the origin of the cocktail Mojito?",
     "answers": {"A": "Cuba",
                 "B": "Spain",
                 "C": "Italy"},
     "correct_answer": "A"},
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
random.shuffle(quiz_data)


def count_keys(quiz_data):
    """
    Counts number of questions in dictionary (this allows more questions to be
    added to dictionary and the intro text to automatically update with number
    of questions).
    This function is based on code taken from the article 'Count Number of
    Keys in Dictionary Python' from DelftStack.
    See credit section of README for more information.
    """
    count = 0
    for i in enumerate(quiz_data):
        count += 1
    return count


num_of_questions = (count_keys(quiz_data))


def start_quiz():
    """
    Starting point of quiz, displays ASCII title text and sushi images. Gets
    user name, shows instructions and asks user if they are ready to begin.
    """
    global name
    name = input("Please type your name and hit the enter key:\n")

    while not name.strip():
        print("Please enter your name to begin the quiz\n")
        name = input("Please type your name and hit the enter key:\n")
    else:
        print(f"Welcome Quizzer {name}!\n")
        print("Take the quiz to test your General knowledge\n")
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


def run_quiz(quiz_data):
    """
    Iterates through quiz questions and potential answers, gets user input and
    implements score by one or zero, depending on user input.
    """
    score = 0
    for entry in quiz_data:
        user_answer = ''
        while user_answer not in ['A', 'B', 'C']:
            print(f"{entry['question']}")

            for key, value in entry['answers'].items():
                print(f"\t{key}: {value}")

            user_answer = input("What is your answer?\n")
            user_answer = user_answer.upper()

            if user_answer not in entry['answers']:
                print("Only a, b or c will be accepted as answers\n")

        if user_answer == entry['correct_answer']:
            print(f"{Fore.GREEN}Correct\n")
            score += 1
        else:
            print(f"{Fore.RED}Oops! Better luck next time\n")

    final_score(score)


def final_score(score):
    """
    Displays final score at end of quiz.
    """

    if score <= 5:
        print(f"Great effort {name}! Your final score is {score} out of\
 {num_of_questions}")
        print("Take the quiz again to see if you can improve your score\n")
    elif score > 5:
        print(f"Congratulations {name}! Your final score is {score} out of\
 {num_of_questions}")


def play_again():
    """
    Asks user if they want to play again. Returns to start of quiz, or ends
    quiz depending on user input.
    """

    restart_quiz = True

    while restart_quiz:
        response = input("Do you want to play again? y/n\n")
        response = response.upper()

        if response == "Y":
            return True
        elif response == "N":
            return False
        else:
            print("That is not a valid option\n")


start_quiz()
run_quiz(quiz_data)


while play_again():
    start_quiz()
    run_quiz(quiz_data)
else:
    print("end of quiz")
    print("click the 'RUN PROGRAM' button to reset the quiz")
