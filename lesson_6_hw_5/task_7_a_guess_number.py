"""
In this module the function guesses users number.
"""


def guess_number_user():
    input('Please, guess number from 1 to 100 and press \'Enter\'')
    start = 1
    stop = 100
    while stop - start > 0:
        number_to_guess = start + (stop - start) // 2
        answer = input(f'Is number equal {number_to_guess}? Answer yes, less or more: ')
        if answer == 'yes':
            print('Thank you for game.')
            break
        elif answer == 'less':
            stop = number_to_guess
        elif answer == 'more':
            start = number_to_guess


def main():
    guess_number_user()


main()
