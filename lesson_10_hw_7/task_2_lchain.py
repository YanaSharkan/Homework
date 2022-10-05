"""
In this module function accepts a lot of iterable (not just lists!) objects, and returns a list of all the elements
of these objects together.
"""

from collections.abc import Iterable


def lchain(*iterables):
    res_list = []
    for el in iterables:
        if isinstance(el, Iterable):
            res_list.extend(list(el))
        else:
            raise TypeError('Only iterables are allowed')
    return res_list


def test_lchain():
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == \
           [1, 2, 3, '5', 6, 7, 8, 9], 'The output should be: [1, 2, 3, \'5\', 6, 7, 8, 9].'
    assert lchain([1, 2, 3], {'5': 5, '6': 6}, tuple((2, 3)), (6, 7), range(8, 10)) == \
           [1, 2, 3, '5', '6', 2, 3, 6, 7, 8, 9], 'The output should be: [1, 2, 3, \'5\', \'6\', 2, 3, 6, 7, 8, 9].'
    try:
        lchain(1)
        assert 2 == 1, 'Should raise an exception'
    except TypeError as err:
        assert str(err) == 'Only iterables are allowed', 'Should raise an exception'


def main():
    test_lchain()
    print(f'Test passed!')


if __name__ == '__main__':
    main()
