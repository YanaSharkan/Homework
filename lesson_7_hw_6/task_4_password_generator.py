"""
This module provides function that generates passwords.
# consists of 8 symbols;
# only lowercase and uppercase latin letters;
# password must contain at least one upper. and one lowercase symbol;
# There should not be more than 2 identical symbols next to each other.
"""

from string import ascii_lowercase

from random import choice, randint


def add_capital_letters(password):
    for i in range(0, 2):
        upper_letter = choice(password)
        password = password.replace(upper_letter, upper_letter.capitalize())
    return password


def add_numbers(password):
    res = [elem for elem in password if elem.islower()]
    return password.replace(choice(res), str(randint(1, 9)), 1)


def add_underscore(password):
    res = [elem for elem in password if elem.islower()]
    return password.replace(choice(res), '_', 1)


def password_generator():
    password = ''
    for i in range(0, 8):
        low_letter = choice(ascii_lowercase)
        if len(password) == 0 or password[-1] != low_letter:
            password += low_letter
        else:
            low_letter = choice(ascii_lowercase.replace(low_letter, ''))
            password += low_letter

    password = add_capital_letters(password)
    password = add_numbers(password)
    password = add_underscore(password)

    return password


def test_password_generator():
    password = password_generator()
    assert len(password) == 8, 'Password len should be 8.'
    assert len([elem for elem in password if elem.islower()]) > 0, 'At least one element should be lowercase.'
    assert len([elem for elem in password if elem.isupper()]) > 0, 'At least one element should be uppercase.'
    assert len([elem for elem in password if elem.isdigit()]) > 0, 'At least one element should be digit.'
    assert len([elem for elem in password if elem == '_']) > 0, 'At least one element should be underscore.'


def main():
    test_password_generator()
    print(f'Suggested password is {password_generator()}')


main()
