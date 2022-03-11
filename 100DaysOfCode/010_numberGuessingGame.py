logo = """
 __  .  .  ___  __   __     ___ .  . .___    .  . .  .  .  .  __  .__  .__  
/ _` |  | |__  /__` /__`     |  |__| |__     |\ | |  |  |\/| |__) |__  |__) 
\__> \__/ |___ .__/ .__/     |  |  | |___    | \| \__/  |  | |__) |___ |  \ 

"""

# Number Guessing Game Objectives:


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


def qa_int_input(question):
    """
    Ensures that the response given by the user can be used in the program
    :param question: The question that will be presented to the player
    :return: Returns valid user response
    """
    while True:
        try:
            response = int(input(question))
            assert response > 0 and response < 101, "Enter a valid number."
        except AssertionError as e:
            print(e)
        except ValueError:
            print("Enter a number.")
        else:
            break
    return response


def qa_str_input(question, options):
    """
    Ensures that the response given by the user can be used in the program.
    :param question: The question that will be presented to the player
    :param options: List of options that can be used by the program
    :return: Returns valid user response
    """
    while True:
        try:
            response = input(question).lower()
            assert response in options, "Select a valid option."
        except AssertionError as e:
            print(e)
        else:
            return response


def establish_level():
    """
    Establishes the difficulty level of game by adjusting number of attempts based on user input.
    :return: Returns the number of initial attempts user will have to guess the number.
    """
    level = qa_str_input("Choose a level by typing 'easy', 'normal', or 'hard': ", ['easy', 'normal', 'hard'])

    if level == 'easy':
        attempts = 10
        print("You have 10 attempts.")
    elif level == 'normal':
        attempts = 7
        print("You have 7 guesses.")
    else:
        attempts = 5
        print("You have 5 guesses.")

    return attempts


def respond():
    """
    Allows user to make a guess. Gives feedback based on response.
    :return: Returns user guess
    """
    response = qa_int_input("Enter your guess: ")
    if response in guesses:
        print(f"You've already guessed {response}, silly!")
    elif response > answer:
        print("  ==> Too high!")
    elif response < answer:
        print("  ==> Too low!")
    else:
        print("  ==> You got it!")
    return response


game_on = 'y'

while game_on == 'y':
    print(logo + "Welcome to the Number Guessing Game.")
    attempts = establish_level()
    answer = random.randint(1, 100)
    response = ''
    guesses = []
    print("\nI'm thinking of a number between 1 and 100. What is it?")

    while attempts > 0 and response != answer:
        response = respond()

        if response not in guesses:
            attempts -= 1
            guesses.append(response)

        if response == answer:
            print(" C O N G R A T U L A T I O N S !")
        elif attempts > 0:
            print(f"\nATTEMPT #{len(guesses) + 1}")
        else:
            print(f"\nGame Over. The number was {answer}")

    game_on = qa_str_input("\nWould you like to play another round? Type 'y' or 'n'. ", ['y', 'n'])
    print("\n" * 10)

input("\nPress [ENTER] to close the program.")
