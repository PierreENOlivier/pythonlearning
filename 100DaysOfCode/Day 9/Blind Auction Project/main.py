# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

def auction_bidding():
    run = True
    bids = {}
    while run:
        # Clear the screen so that the next user does not see previous bid
        clear_screen = "\n" * 100
        print(clear_screen)

        print(logo)

        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))

        bids[name] = bid

        ans = input("Are there any other bidders? Type 'yes' or 'no. \n")

        if ans == "no":
            run = False

    print(bids.items())

    # find_highest_bidder(bids)
    find_highest_bidder_max(bids)


def find_highest_bidder(
    bid_dictionary: dict
):
    highest_bidder = ""
    for key in  bid_dictionary:
        print(f"Current highest: {highest_bidder}")
        if highest_bidder == "":
            highest_bidder = key
        else:
            if bid_dictionary[key] > bid_dictionary[highest_bidder]:
                highest_bidder = key


    print(f"Highest bidder is {highest_bidder} with ${bid_dictionary[highest_bidder]}!")


def find_highest_bidder_max(
    bid_dictionary: dict
):
    highest_bidder = max(bid_dictionary, key = bid_dictionary.get)

    print(f"Highest bidder is {highest_bidder} with ${bid_dictionary[highest_bidder]}!")


auction_bidding()


