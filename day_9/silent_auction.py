"""
day_9
Created February 03, 2022 by Jennifer Baughman

Description:
"""


def get_bid():
    try:
        bid = int(input("What's your bid? "))
        return bid
    except ValueError:
        print("That is not a valid bid. Please type a whole number.")
        get_bid()


def main():
    print("Welcome to the secret auction.")
    no_bidders = False
    bids = dict()
    while not no_bidders:
        name = input("What is your name? ")
        bid = get_bid()
        bids[name] = bid
        more_bidders = input(
                "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if more_bidders == 'yes':
            print("\n" * 50)
            continue
        else:
            no_bidders = True
    winner = max(bids.items(), key=lambda x: x[1])
    print(f"The winner is {winner[0]} with a bid of ${winner[1]}.")


if __name__ == "__main__":
    main()
