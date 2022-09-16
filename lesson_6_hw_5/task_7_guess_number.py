"""
In this module the function allows user to guess a number.
"""

import random


def guess_number():
    num = random.randint(1, 11)
    num_from_user = None
    while num_from_user != num:
        num_from_user = int(input("Enter a number between 1 and 10: "))
        if num_from_user == num:
            print('You guessed!')
            break
        elif num_from_user > num:
            print('No, enter less number.')
        elif num_from_user < num:
            print('No, enter bigger number.')


def main():
    guess_number()


main()
