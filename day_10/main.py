"""
calculator
Created February 04, 2022 by Jennifer Baughman

Description:
"""

from art import logo
from operator import add, sub, mul, truediv
from sys import exit


def get_int(message):
    try:
        num = int(input(f"{message}"))
        return num
    except ValueError:
        print("That is not a valid number. Please enter an integer.\n")
        get_int()


def get_operator():
    try:
        text = input("Pick an operation:")
        if text not in ['+', '-', '*', '/']:
            raise ValueError
        return text
    except ValueError:
        print("That is not a valid operator.\n")
        get_operator()


def main():
    print(logo)
    operators = {"+": add, "-": sub, "*": mul, "/": truediv}
    current_calculation = True
    operand_1 = get_int("What's the first number?: ")
    while current_calculation:
        for sym in operators.keys():
            print(sym)
        op_symbol = get_operator()
        op = operators[op_symbol]
        operand_2 = get_int("What's the next number?: ")
        output = op(operand_1, operand_2)
        print(
                f"{operand_1} {op_symbol} {operand_2} = "
                f"{output}")
        con_calc = input(
                f"Type 'y' to continue calculating with {output}, type 'n' to "
                f"start a new calculation, or type 'q' to quit: ").lower()
        if con_calc == 'y':
            operand_1 = output
        elif con_calc == 'q':
            print("Goodbye!")
            exit()
        else:
            operand_1 = get_int("What's the first number?: ")


if __name__ == '__main__':
    main()
