#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number.

    Args:
        number (int, float): The number to print the last digit of.

    Returns:
        int: The last digit of the number.
    """
    print(abs(number) % 10, end="")
    return abs(number) % 10
