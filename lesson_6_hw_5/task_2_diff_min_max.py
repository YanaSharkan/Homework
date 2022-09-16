"""
This module finds the difference between the maximum and minimum value
of the given limit.
"""

import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    """
    This function uses built-in Python's min() and max() functions.
    """

    random_list = []

    for i in range(num_limit):
        random_list.append(random.randint(lower_bound, upper_bound))

    min_num = min(random_list)
    max_num = max(random_list)
    return max_num - min_num


def diff_min_max_2a(num_limit, lower_bound, upper_bound):
    """
    This function without built-in Python's min() and max() functions.
    """

    random_list = []
    min_num = upper_bound
    max_num = lower_bound

    for i in range(num_limit):
        random_list.append(random.randint(lower_bound, upper_bound))

    for n in random_list:
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n

    return max_num - min_num


def test_diff_min_max():
    assert diff_min_max(1, 0, 0) == 0, 'Result is invalid for params for 1, 0, 0'
    assert diff_min_max(100, 2, 3) == 1, 'Result is invalid for params for 100, 2, 3'


def test_diff_min_max_2a():
    assert diff_min_max_2a(1, 0, 0) == 0, 'Result is invalid for params for 1, 0, 0'
    assert diff_min_max_2a(100, 2, 3) == 1, 'Result is invalid for params for 100, 2, 3'


def main():
    test_diff_min_max()
    test_diff_min_max_2a()
    num_limit = int(input('Enter amount of numbers to generate: '))
    lower_bound = int(input('Enter lower bound: '))
    upper_bound = int(input('Enter upper bound: '))
    res_1 = diff_min_max(num_limit, lower_bound, upper_bound)
    print(f'The difference between min and max is {res_1}')
    res_2 = diff_min_max_2a(num_limit, lower_bound, upper_bound)
    print(f'The difference between min and max is {res_2} (Version 2a)')


main()
