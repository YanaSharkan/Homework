"""
This module returns the largest digit of a randomly generated 12-digit natural number.
"""

import random


def get_max_digit_str(num):
    """
    Function returns the largest digit of the number with using strings.
    """
    max_digit = 0
    for digit in str(num):
        digit_int = int(digit)
        if digit_int > max_digit:
            max_digit = digit_int
    return max_digit


def get_max_digit(num):
    """
    Function returns the largest digit of the number without using strings.
    """
    max_digit = 0
    numbers = num
    while numbers > 0:
        digit = numbers % 10
        if digit > max_digit:
            max_digit = digit
        numbers = numbers // 10
    return max_digit


def test_get_max_digit_str():
    assert get_max_digit_str(123456789123) == 9, 'Wrong largest digit.'
    assert get_max_digit_str(111111111111) == 1, 'Wrong largest digit.'


def test_get_max_digit():
    assert get_max_digit_str(123456789123) == 9, 'Wrong largest digit.'
    assert get_max_digit_str(111111111111) == 1, 'Wrong largest digit.'


def main():
    number = random.randint(10 ** 11, 10 ** 12)

    test_get_max_digit_str()
    test_get_max_digit()

    num = get_max_digit_str(number)
    print(f'The biggest digit (with using str) is: {num}')

    num_1 = get_max_digit(number)
    print(f'The biggest digit (without using str) is: {num_1}')


main()
