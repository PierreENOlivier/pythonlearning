from random import randint
from art import logo
from typing import List, Tuple

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(
    n: int
) -> List[int]:
    """
    Generate a hand of n cards
    :param n: n number of cards to draw
    :return: List of n cards
    """
    index = []
    for i in range(n):
        index.append(randint(0, len(cards) - 1))

    return [cards[ind] for ind in index]


def check_for_flip(current_hand: List[int]) -> List[int]:
    """
    Check whether an Ace should be flipped into a 1
    :param current_hand: A list containing the hand of a player or dealer
    :return: A modified list
    """
    current_hand_copy = current_hand.copy()

    if sum(current_hand_copy) > 21:
        if 11 in current_hand_copy:
            current_hand_copy.remove(11)
            current_hand_copy.append(1)

    return current_hand_copy


def ask_hit(current_hand: List[int]) -> List[int]:
    """
    Adds new card to current hand
    :param current_hand: List of cards in hand
    :return: Updated hand with new cards
    """
    new_card = draw_card(1)
    current_hand = current_hand + new_card
    # Need to flip ACE when the score goes bust
    if sum(current_hand) > 21:
        current_hand = check_for_flip(current_hand)

    return current_hand


def compare_score(player_hand: list, dealer_hand: list):
    """
    Compares the score of player and dealer hands
    :param player_hand: A list containing the player's cards
    :param dealer_hand: A list containing the player's cards
    :return:
    """
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    if player_score == 21 & len(player_hand) == 2:
        return "Blackjack! You win!"

    elif dealer_score == 21 & len(dealer_hand) == 2:
        return "Blackjack! But not your hand, you lose!"

    elif player_score == dealer_score:
        return "It is a draw!"

    elif player_score > 21:
        return "Busted! You lose!"

    elif dealer_score > 21:
        return "Dealer busted! You win!"

    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"


def calculate_score(
        player_hand: List[int],
        dealer_hand: List[int]
) -> Tuple[int, int]:
    """
    Calculate respective scores of player and dealer
    :param player_hand: List of cards in player's hand
    :param dealer_hand: List of cards in dealer's hand
    :return: A tuple containing the respective score
    """
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    return player_score, dealer_score


def print_hands(
        player_hand: List[int],
        dealer_hand: List[int],
        hide_dealer: bool = True
) -> None:
    """
    Prints the current hands of player and dealer
    :param player_hand: List of cards in player's hand
    :param dealer_hand: List of cards in dealer's hand
    :param hide_dealer: If True, reveals the first card of the dealer only
    :return: None
    """
    player_score, dealer_score = calculate_score(player_hand, dealer_hand)
    print(f"Your cards: {player_hand}, score: {player_score}")
    if hide_dealer:

        dealer_hand_hidden = [
            str(card) if ind == 0 else '*' for ind, card
            in enumerate(dealer_hand)
        ]
        print(f"Dealer's card: {dealer_hand_hidden}")

    else:
        print(f"Dealer's card: {dealer_hand}, score: {dealer_score}")

    print("-" * 20)


def play_blackjack():
    """
    Game interface allows playing several rounds
    :return:
    """
    run_game = True
    while run_game:
        choice = input("Would you like to play a game? (y/n): ")

        if choice == "n":
            run_game = False
        else:
            print("\n" * 20)
            print(logo)
            play_game()


def play_game():
    """
    Game interface to play one game of blackjack
    :return:
    """
    # Draw first hand player
    player_hand = draw_card(2)
    dealer_hand = draw_card(2)

    is_turn_over = False
    while not is_turn_over:
        player_score, dealer_score = calculate_score(player_hand, dealer_hand)
        print_hands(player_hand, dealer_hand, hide_dealer=True)

        if (player_score == 21 and len(player_hand) == 2) or player_score > 21:
            is_turn_over = True
        else:
            choice = input("Do you want to (H)it or (P)ass? ")
            if choice == "H":
                player_hand = ask_hit(player_hand)
                print_hands(player_hand, dealer_hand, hide_dealer=True)

            else:
                is_turn_over = True

    print("-" * 20)
    print("Dealer playing")
    print_hands(player_hand, dealer_hand, hide_dealer=False)

    player_score, dealer_score = calculate_score(player_hand, dealer_hand)
    while player_score < 21 and dealer_score < 17:
        dealer_hand = ask_hit(dealer_hand)
        print_hands(player_hand, dealer_hand, hide_dealer=False)
        player_score, dealer_score = calculate_score(player_hand, dealer_hand)

    msg = compare_score(player_hand, dealer_hand)
    print(msg)

play_blackjack()