"""
day_two_tip_calculator
Created January 29, 2022 by Jennifer Baughman

Description: Day Two Udemy 100 Days of Code: Python Bootcamp 2022
Create a tip calculator.
"""


def validate_input(message):
    data = input(message)
    try:
        data = float(data)
    except ValueError:
        print("Please enter a numeric value.")
        validate_input(message)
    return data


def calculate_share(total_bill, split, tip):
    share = total_bill / split
    tip_amt = share * (tip / 100)
    return share + tip_amt


def main():
    print("Welcome to the tip calculator.")
    total_bill = validate_input("What was the total bill? $")
    split = validate_input("How many people to split the bill? ")
    tip = validate_input(
            "What percentage tip would you like to give? 15, 20, or 25? ")
    print(
        f"Each person should pay: $"
        f"{calculate_share(total_bill, split, tip):.2f}")


if __name__ == "__main__":
    main()
