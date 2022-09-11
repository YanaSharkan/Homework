"""
This program checks if year is a leap year.
"""


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def test_is_leap_year():
    assert is_leap_year(2004) is True, 'Invalid result for 2004'
    assert is_leap_year(2000) is True, 'Invalid result for 2000'
    assert is_leap_year(1900) is False, 'Invalid result for 1900'


def main():
    year = int(input('Please, enter year: '))
    test_is_leap_year()
    res = is_leap_year(year)
    if res is True:
        print('It is a leap year')
    else:
        print('It is not a leap year')


main()
