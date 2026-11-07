from art import logo, vs
from game_data import data
from random import choice

compare_data = data.copy()

def print_fight(data_A: dict, data_B: dict, score) -> None:
    """
    Take data from A and B and print the interface
    :param data_A: Data dict from side A
    :param data_B: Data dict from side A
    :return: None
    """
    print(logo)

    if score > 0:
        print(f"Current Score: {score}")


    print(
        "Compare A: "
        f"{data_A['name']}, "
        f"a {data_A['description']}, "
        f"from {data_A['country']}"
    )

    print(vs)

    print(
        "Against B: "
        f"{data_B['name']}, "
        f"a {data_B['description']}, "
        f"from {data_B['country']}"
    )


def check_answer(
        answer: str,
        value_A: int,
        value_B: int) -> bool:
    """

    :param answer: A string containing the answer 'A' or 'B'
    :param value_A: The value of A to compare against B
    :param value_B: The value of B to compare against A
    :return: True if the answer is correct, False otherwise
    """
    if answer == 'A' and value_A >= value_B:
        return True
    elif answer == 'B' and value_B >= value_A:
        return True
    else:
        return False

def prompt_valid_answer():
    """
    Prompt the user and check validity of the answer
    :return:
    """
    while True:
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer in ["A", "B"]:
            break
        else:
            print("Answer must be 'A' or 'B'")
    return answer


def print_eval_score(score_tracker: int) -> None:
    """
    Evaluate the final score and return a comment
    :param score_tracker: Final score of the player
    :return:
    """

    if score_tracker > 100:
        print(f"{score_tracker}!!! Really! That's pretty high!")
    elif score_tracker > 50:
        print(f"{score_tracker} is quite good, but you can do better! I know it!")
    elif score_tracker > 20:
        print(f"{score_tracker}... You're getting there, try again!")
    elif score_tracker > 5:
        print(f"{score_tracker}... I guess that's a start... Try again!")
    elif score_tracker > 0:
        print(f"{score_tracker} kinda sucks... But at least it is not 0!")
    else:
        print(f"Jeez! {score_tracker}?! Really?! You really suck at this...")

def prompt_play_again(
        prompt,
        if_true,
        if_false
):
    """

    :param prompt: Prompt to display to the user
    :param if_true: Expected answer if True
    :param if_false: Expected answer if False
    :return: Boolean for loop control
    """

    answer = input(f"{prompt} Type {if_true} or {if_false}: ")

    if answer == if_true:
        return True
    elif answer == if_false:
        return False


def higher_or_lower(
        game_data:dict
):
    """
    Game loop for higher or lower.

    :param game_data: A dictionary containing game data
    :return: None
    """

    play_game = True
    while play_game:

        all_indices = [ind for ind in range(len(game_data))]
        print(f"all indices: {all_indices}")

        side_A_ind = choice(all_indices)
        previously_used_indices = []
        previously_used_indices.append(side_A_ind)

        score_tracker = 0
        not_lost = True
        while not_lost:
            available_indices = [ind for ind in all_indices if ind != previously_used_indices]
            side_B_ind = choice(available_indices)

            side_A = game_data[side_A_ind]
            side_B = game_data[side_B_ind]

            print_fight(side_A, side_B, score_tracker)

            # print(f"Side A: {side_A['follower_count']} | Side B: {side_B['follower_count']} | Score: {score_tracker}")

            answer = prompt_valid_answer()

            # Check the guess
            guessed = check_answer(
                answer,
                side_A['follower_count'],
                side_B['follower_count']
            )

            if score_tracker + guessed > score_tracker:
                score_tracker = score_tracker + guessed
            else:
                not_lost = False


            if not_lost:
                # Assign B for next round
                side_A_ind = side_B_ind
                # Keep track of what has been used to avoid reusing it immediately
                previously_used_indices.append(side_B_ind)

            # Progressively flush which data has been used
            if len(previously_used_indices) > 5:
                previously_used_indices.pop(0)

            print("\n" * 20)

        print(f"Sorry, that's wrong! Final score: {score_tracker}")
        print_eval_score(score_tracker)

        play_game = prompt_play_again(
            prompt="Would you like to play again?",
            if_true="y",
            if_false="n"
        )





higher_or_lower(compare_data)


