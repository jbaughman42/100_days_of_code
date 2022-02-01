"""
password_generator
Created January 31, 2022 by Jennifer Baughman

Description:
"""
import string
from random import shuffle, randint, choice


def main():
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters do you want in your password? "))
    num_symbols = int(input("How many symbols do you want? "))
    num_digits = int(input("How many numbers do you want? "))
    pwd_chars = []
    for _ in range(num_digits):
        pwd_chars.append(str(randint(0, 9)))
    for _ in range(num_symbols):
        symbols = ['!', '@', '#', '$', '%', '&']
        pwd_chars.append(choice(symbols))
    for _ in range(num_letters):
        pwd_chars.append(choice(string.ascii_letters))
    shuffle(pwd_chars)
    print(f"Here is your password: {''.join(pwd_chars)}")


if __name__ == "__main__":
    main()
