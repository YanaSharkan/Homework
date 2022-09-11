"""
This program checks the sign of number.
"""


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def test_sign():
    assert sign(10) == 1, 'Invalid result for 10'
    assert sign(-10) == -1, 'Invalid result for -10'
    assert sign(0) == 0, 'Invalid result for 0'


def main():
    test_sign()
    number = int(input('Enter a number to check: '))
    res = sign(number)
    print(f'The sign for number is {res}')


main()
