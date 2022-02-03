"""
caesar_cipher
Created February 03, 2022 by Jennifer Baughman

Description:
"""
import string


def get_cipher_type():
    # Basic input validation for cipher
    cipher = ""
    while cipher not in ('encode', 'decode'):
        cipher = input(
                "Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    return cipher


def get_shift():
    try:
        shift = int(input("Type the shift number:\n"))
        return shift
    except ValueError:
        print(
                "That is not a valid shift number. Please type a whole number "
                "between 0 and 26.\n")
        get_shift()


def caesar(message, cipher, shift):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = []
    if cipher == 'decode':
        shift *= -1
    for l in message:
        new_index = letters.index(l) + shift
        if new_index > 25:
            new_index -= 26
        elif new_index < 0:
            new_index += 26
        output.append(letters[new_index])
    return ''.join(output)


def main():
    end = False
    while not end:
        cipher = get_cipher_type()
        message = input("Type your message:\n")
        shift = get_shift()
        output = caesar(message, cipher, shift)
        print(f"Here's the {cipher}d result: {output}")
        go_again = input(
                "Type 'yes' if you want to go again. Otherwise type "
                "'no'.\n").lower()
        end = False if go_again == 'yes' else True


if __name__ == "__main__":
    main()
