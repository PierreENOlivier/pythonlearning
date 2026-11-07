from random import randint
from typing import Tuple

BANNER = r"""
  ________                              .__  __   
 /  _____/ __ __   ____   ______ ______ |__|/  |_ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |  \   __\
\    \_\  \  |  /\  ___/ \___ \ \___ \  |  ||  |  
 \______  /____/  \___  >____  >____  > |__||__|  
        \/            \/     \/     \/            
"""

GAME_OVER = r"""
 _______  _______  _______  _______    _______           _______  _______ 
(  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
| (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
| |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
| | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
| | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
| (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
(_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
                                                                          
"""

def set_difficulty() -> int:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    print(f"You get {attempts} attempts to guess the number.")
    return attempts


def check_guess(
        guess: int,
        expected: int,
        remaining_attempts: int
) -> Tuple[bool, int]:
    """

    :param guess:
    :param expected:
    :param remaining_attempts:
    :return: A tuple with True if guessed, False otherwise and
        the updated remaining number of attempts
    """
    is_guessed = False
    if guess == expected:
        print(f"Correct! The answer was {expected}")
        is_guessed = True
    elif guess > expected:
        remaining_attempts -= 1
        print("Too high.")
    else:
        remaining_attempts -= 1
        print("Too low.")

    return is_guessed, remaining_attempts

def check_attempts(
        attempts: int,
        expected_answer: int
) -> None:
    """
    :param attempts: Remaining number of attempts
    :param expected_answer: The expected number
    :return: None, printing status of game
    """
    if attempts > 0:
        print("Guess again.")
        print(f"{"-" * 10}")
        print(f"You have {attempts} attempts remaining...")
    else:
        print(GAME_OVER)
        print("You have run out of guesses. ")
        print(f"The answer was {expected_answer}... "
              "Better luck next time!")



def guess_it():
    """Guess the number"""
    game_loop = True
    while game_loop:
        print(BANNER)
        print("Welcome to Number Guessing Game!")

        expected_number = randint(1, 100)
        print("I am thinking of a number between 1 and 100.")

        attempts = set_difficulty()

        is_guessed = False
        previous_guesses = []
        while attempts > 0 and not is_guessed:
            if len(previous_guesses) > 0:
                previous_guess_str = [str(i) for i in previous_guesses]
                print(f"You have tried: {', '.join(previous_guess_str)}.")



            guess = int(input("Take a guess: "))
            previous_guesses.append(guess)
            is_guessed, attempts = check_guess(
                guess,
                expected_number,
                attempts
            )

            if not is_guessed:
                check_attempts(
                    attempts,
                    expected_number
                )




        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "n":
            game_loop = False
        else:
            print(f"{'\n' * 20}")


guess_it()