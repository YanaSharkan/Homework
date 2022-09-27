"""
This module provides function that generates passwords.
# consists of 8 symbols;
# only lowercase and uppercase latin letters;
# password must contain at least one upper. and one lowercase symbol;
# There should not be more than 2 identical symbols next to each other.
"""

from string import ascii_lowercase, ascii_uppercase, digits

from random import choice


def is_valid_password(password):
    for i, s in enumerate(password):
        if i > 0 and s == password[i - 1]:
            return False

    has_lower_characters = len([elem for elem in password if elem.islower()]) > 0
    has_upper_characters = len([elem for elem in password if elem.isupper()]) > 0
    has_number_characters = len([elem for elem in password if elem.isdigit()]) > 0
    has_special_characters = len([elem for elem in password if elem == '_']) > 0
    return has_lower_characters and has_upper_characters and has_number_characters and has_special_characters


def password_generator():
    symbols = ascii_lowercase + ascii_uppercase + digits * 3 + '_' * 20

    while True:
        password = ''
        for i in range(0, 8):
            symbol = choice(symbols)
            password += symbol

        if is_valid_password(password):
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
