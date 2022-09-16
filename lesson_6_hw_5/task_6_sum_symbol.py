"""
In this module function calculates the sum of the Unicode codes of all characters between and
inclusive of the given two characters.
"""


def sum_symbol_codes(first, last):
    first_code = ord(first)
    second_code = ord(last) + 1
    total = 0
    for i in range(first_code, second_code):
        total += i
    return total


def test_sum_symbol_codes():
    assert sum_symbol_codes('a', 'd') == 394, 'Must be equal 294'
    assert sum_symbol_codes('1', '2') == 99, 'Must be equal 99'


def main():
    test_sum_symbol_codes()
    symbol_1 = input('Enter first symbol:')
    symbol_2 = input('Enter second symbol:')
    sum_symbols = sum_symbol_codes(symbol_1, symbol_2)
    print(f'The sum is: {sum_symbols}')


main()
