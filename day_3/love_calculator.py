"""
day_three_love_calculator
Created January 29, 2022 by Jennifer Baughman

Description:
"""


def check_letters(name_1, name_2, word):
    """Checks to see how many times the letters in name_1 and name_2
    exist in word.
    
    Args:
        name_1: (str) first name
        name_2: (str) second name
        word: word with letters

    Returns: (int) total count of letters
    """
    all_name_letters = list(
            name_1.upper().strip(" ") + name_2.upper().strip(" "))
    letter_counts = {l: all_name_letters.count(l) for l in word}
    return sum(letter_counts.values())


def love_score(true, love):
    score = int(str(true) + str(love))
    if score < 10 or score > 90:
        return f"Your score is {score}; you go together like Coke and Mentos."
    elif 40 <= score <= 50:
        return f"Your score is {score}; you're alright together."
    else:
        return f"Your score is {score}; you figure it out!"


def main():
    print("Welcome to the Love Calculator!")
    name_1 = input("What is your name? \n")
    name_2 = input("What is their name? \n")
    true = check_letters(name_1, name_2, "TRUE")
    love = check_letters(name_1, name_2, "LOVE")
    print(love_score(true, love))


if __name__ == '__main__':
    main()
