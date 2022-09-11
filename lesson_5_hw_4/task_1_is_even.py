"""
This module checks does number is even.
"""


def is_even(number):
    return number % 2 == 0


def test_is_even():
    assert is_even(6) is True, 'The remainder after dividing by two must be 0.'
    assert is_even(5) is False, 'The remainder after division by two is not 0.'


def main():
    number = int(input('Enter number: '))
    test_is_even()
    res = is_even(number)
    if res:
        print('Number is even.')
    else:
        print('Number is odd.')



main()
