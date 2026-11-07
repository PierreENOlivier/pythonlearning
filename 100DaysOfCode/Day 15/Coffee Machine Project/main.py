import pprint
import string
import math
import time
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COIN_SYMBOLS = {
    'quarters': '🟡',
    'dimes': '⚪',
    'nickels': '🟠',
    'pennies': '🟤',
}

def coffee_selector():
    """
    Get input from user
    :return: a string containing order
    """
    coffees = [k for k in MENU.keys()]

    coffee_mapping = format_menu_mapping(coffees)
    menu_text = flatten_menu_mapping(coffee_mapping)

    print("“What would you like?\n")
    mapping_keys = [k for k,v in coffee_mapping.items()]

    choice = input(f"{menu_text}:  ")
    if choice in mapping_keys:
        choice = coffee_mapping[choice]

    return choice

def print_report(
        state,
        with_cash: bool,
        raw_output:bool=False
):
    """
    Print a report of the inventory
    :param state: a dictionary containing levels of different ingredients
    :return:
    """
    if raw_output:
        pprint.pprint(state)
    else:
        print(
            f"Water: {state['inventory']['water']}mL\n"
            f"Milk: {state['inventory']['milk']}mL\n"
            f"Coffee: {state['inventory']['coffee']}g\n"
            f"Money: ${calculate_total_coins(state['money'])}\n" if with_cash else ""
        )


def calculate_total_coins(coins):
    """
    Calculate total of coins from dictionary of coins and quantities
    :param coins: Dictionary containing types of coins, their face value and quantities
    :return: A float showing the value
    """
    total = 0
    for key, value in coins.items():
        total += coins[key]['value'] * coins[key]['quantity']

    return total

def insert_coins(cost):
    """
    Check cost against provided money and give back change
    :param cost:
    :return:
    """


    change = {
        'quarters': {'value': 0.25, 'quantity': 0},
        'dimes': {'value': 0.10, 'quantity': 0},
        'nickels': {'value': 0.05, 'quantity': 0},
        'pennies': {'value': 0.01, 'quantity': 0},
    }

    for key, coin_data in change.items():
        print("\033[H\033[J", end="")
        remaining = max(
            round(
                cost - calculate_total_coins(change),
                2
            ),
            0
        )

        if remaining == 0:
            continue

        print(f"Please insert coins {COIN_SYMBOLS[key]}.")
        print(f"Remaining: ${remaining}.")
        quant = input(f"How many {key} (${coin_data['value']})?: ")
        if quant == '':
            change[key]['quantity'] = 0
        else:
            change[key]['quantity'] = int(quant)




    return change

def is_enough_money(
        wallet:dict,
        product: str
) -> (float, bool):
    """

    :param wallet: A dictionary containing the cash inserted by user
    :param product: A str containing the choice of beverage
    :return: A tuple containing the cash difference and status whether enough money was inserted
    """
    cost = MENU[product]['cost']

    total_wallet = calculate_total_coins(wallet)
    # Check if enough
    difference = round(total_wallet - cost, 2)
    is_enough = True if difference >= 0.0 else False

    if not is_enough:
        print(f"You are ${cost - total_wallet} short. Money will be refunded.")

    return difference, is_enough

def payment_terminal(
        state_machine: dict,
        choice: str) -> (dict, dict, bool):
    """
    Payment terminal handling payment and returning the status of the transaction
    :param status_machine: A dictionary containing the inventory and money state of the machine
    :param choice: A string containing the selected beverage option
    :return: A tuple containing the updated state of the machine, cash change and the status of the transaction
    """
    # Insert coins
    cost = MENU[choice]['cost']
    print(f"Beverage: {choice} | Cost: ${cost}")
    wallet_user = insert_coins(cost)

    # Check value
    cash_difference, status_money = is_enough_money(wallet_user, choice)

    # Handle cash
    if status_money:
        # calculate change
        wallet_user, wallet_machine, any_change=(
            calculate_change(cash_difference, wallet_user, state_machine['money'])
        )
        status_transaction = True

    else:
        print("Refunding money...")
        print_wallet(wallet_user)
        status_transaction = False

    return state_machine, wallet_user, status_transaction

def calculate_change(
        price_difference: float,
        wallet_user: dict,
        wallet_machine: dict
) -> (dict, dict, bool):
    """
    Process coins from the user and those in the machine to return change
    :param price_difference:
    :param wallet_user:
    :param wallet_machine:
    :return: A wallet to return to the user, an updated wallet of the machine, status whether any change
    """

    # Should check if enough coins in machine for change

    # Convert to integer cents to handle float point precision
    wallet_machine_int = convert_wallet_to_integer_cents(wallet_machine)
    wallet_user_int = convert_wallet_to_integer_cents(wallet_user)

    price_difference_int = int(price_difference * 100)

    for key, value in wallet_machine_int.items():
        wallet_machine_int[key]['quantity'] += wallet_user_int[key]['quantity']
        wallet_user_int[key]['quantity'] = 0

    if price_difference_int > 0:
        # update user wallet
        while calculate_total_coins(wallet_user_int) != price_difference_int:
            for key, coins in wallet_machine_int.items():
                remaining_change = price_difference_int - calculate_total_coins(wallet_user_int)
                quantity_of_coin = min(
                    math.floor(remaining_change / coins['value']),
                    coins['quantity']
                )

                wallet_user_int[key]['quantity'] += quantity_of_coin
                wallet_machine_int[key]['quantity'] -= quantity_of_coin


        any_change = True
    else:
        any_change = False

    wallet_user = convert_wallet_to_float(wallet_user_int)
    wallet_machine = convert_wallet_to_float(wallet_machine_int)

    return wallet_user, wallet_machine, any_change

def print_wallet(wallet: dict) -> None:
    print("-" * 10)
    for key, coin_data in wallet.items():
        print(f"{str(key).title()} (${coin_data['value']}): {coin_data['quantity']} | "
              f"Total: ${coin_data['quantity'] * coin_data['value']}"
        )
    print(f"Grand Total: ${calculate_total_coins(wallet)}")
    print("-" * 10)

def convert_wallet_to_integer_cents(wallet: dict) -> dict:
    for key, coin_data in wallet.items():
        wallet[key]['value'] = int(wallet[key]['value'] * 100)
    return wallet

def convert_wallet_to_float(wallet: dict) -> dict:
    for key, coin_data in wallet.items():
        wallet[key]['value'] = round(float(wallet[key]['value'] / 100), 2)
    return wallet

def format_menu_mapping(selection):
    """
    Take list of options and returns a mapping to letters

    :param selection: A string containing options
    :return: A mapping {LETTER: Option}
    """
    n_items = len(selection)
    letters_menu = string.ascii_uppercase[:n_items]
    mapping = {key: value for key, value in zip(letters_menu, selection)}

    return mapping

def flatten_menu_mapping(selection_mapping):
    """
    Flattens a mapping into a human-readable string
    :param selection_mapping: A dictionary mapping {LETTERS: Option}
    :return: A string in the form '(A) Option A, (B) Option B'
    """
    menu_list = [
        f"({str(key).upper()}) {str(value).upper()}" for key, value in selection_mapping.items()
    ]
    menu_string = ", ".join(menu_list)
    return menu_string

def are_ingredients_available(
        choice: str,
        state: dict
) -> bool:
    """
    Checks availability of ingredients
    :param choice: Choice of beverage
    :param state: State of machine with inventory
    :return: True if all available, False otherwise
    """
    ingredients = MENU[choice]['ingredients']
    ingredients_in_machine = state['inventory']
    n_ingredients = len(ingredients.keys())

    missing_ingredients = []
    for ingredient in ingredients.keys():
        quantity_needed = ingredients[ingredient]
        quantity_available = ingredients_in_machine[ingredient]

        if quantity_available < quantity_needed:
            missing_ingredients.append(ingredient)

    if len(missing_ingredients) > 0:
        missing_str = ", ".join(missing_ingredients)
        print(f"Sorry, there is not enough {missing_str}.")

    return len(missing_ingredients) == 0

def idle_waiting_refill(state):
    print(
        f"Current Inventory" +
        f"\n" +
        f"{'-' * 10}"
    )
    print_report(state)
    print("\n")

    empty = True
    while empty:
        ans = input("Is the machine refilled? (y/n): ")
        if ans == "y":

            for key, value in resources.items():
                state['inventory'][key] = value
            empty = False


    print_report(state, with_cash=False)
    return state

def make_coffee(
        choice: str,
        state_machine: dict
) -> dict:
    """
    Prepare beverage
    :param choice: String containing beverage choice
    :param state_machine: Dictionary containing state of the machine
    :return: Return the state of the machine
    """

    animation_sequence = ["empty", "half_full", "full", "ready"]
    art_coffee = {
'empty':
r"""
+-----------------------+
|     NESPRESSO         |
|         ||            |
|         vv            |
|                       |
|      \      /_        |
|       \    /__)       |
|        \__/           |
|  ===================  |
+-----------------------+
""",

'half_full':
r"""
+-----------------------+
|     NESPRESSO         |
|         ||            |
|         vv            |
|                       |
|      \      /_        |
|       \----/__)       |
|        \__/           |
|  ===================  |
+-----------------------+
""",

'full':
r"""
+-----------------------+
|     NESPRESSO         |
|         ||            |
|         vv            |
|                       |
|      \------/_        |
|       \    /__)       |
|        \__/           |
|  ===================  |
+-----------------------+
""",

'ready':
r"""
+-----------------------+
|     NESPRESSO         |
|         ||            |
|         vv            |
|      ________         |
|      \------/_        |
|       \    /__)       |
|        \__/           |
|  ===================  |
+-----------------------+
"""
    }

    recipe = MENU[choice]['ingredients']
    for ingredient, value in recipe.items():
        state_machine['inventory'][ingredient] -= value

    size_refresh = max([frame.count("\n") for frame in art_coffee.values()])

    for i, frame in enumerate(animation_sequence):
        print("\033[2J\033[H", end="")
        print(f"\r{art_coffee[frame]}", end="", flush=True)

        time.sleep(1)

    return state_machine

def print_change(wallet):
    coin_list = []
    for key, coin_data in wallet.items():
        if coin_data['quantity'] == 0:
            continue
        coin_str = f"{COIN_SYMBOLS[key]} {coin_data['quantity']}"
        coin_list.append(coin_str)


    exchange_str = (f"Your change: ${round(calculate_total_coins(wallet), 2)}: "
                    f"{'  '.join(coin_list)}")

    print(exchange_str)

def print_loading_bar():
    for i in range(10):
        print(f"\r[{'█' * i}]", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def machine_interface_loop():
    machine_is_on = True
    state_machine = {}
    state_machine['inventory'] = resources.copy()
    # pprint.pprint(state_machine)

    ### TEST EMPTY
    # state_machine['inventory']['water'] = 0
    # state_machine['inventory']['coffee'] = 10
    ###

    change_in_machine = {
        'quarters': {'value': 0.25, 'quantity': 10},
        'dimes': {'value': 0.10, 'quantity': 20},
        'nickels': {'value': 0.05, 'quantity': 50},
        'pennies': {'value': 0.01, 'quantity': 100},
    }
    state_machine['money'] = change_in_machine

    # pprint.pprint(state_machine)

    while machine_is_on:
        print("\n" * 25, end="")
        print("\033[2J\033[H", end="")
        print("back to menu")
        print("-" * 20)

        statuses = {}

        choice = coffee_selector()

        if choice == "report":
            print_report(state_machine)
        elif choice == "off":
            machine_is_on = False
        else:
            statuses["ingredients"] = are_ingredients_available(choice, state_machine)
            if not statuses["ingredients"]:
                state_machine = idle_waiting_refill(state_machine)

            # Process payment
            state_machine, user_coin_change, statuses["payment"] = payment_terminal(state_machine, choice)

            # Issue, if refill inventory, it skips payment
            # Likely because previous round does not reset status

            if statuses["payment"]:
                print_loading_bar()
                print("💳 Payment successful. ✅")
                time.sleep(2)
                state_machine = make_coffee(choice, state_machine)

            if calculate_total_coins(user_coin_change) > 0:
                print_change(user_coin_change)

        time.sleep(2)



machine_interface_loop()