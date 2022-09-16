"""
This program find the difference between the sum of all even numbers and the sum of all odd numbers,
between the num_limit random numbers generated in the given range.
"""

import random


def diff_odd_even(num_limit, lower_bound, upper_bound):
    random_list = []
    odd_sum = 0
    even_sum = 0

    for i in range(num_limit):
        random_list.append(random.randint(lower_bound, upper_bound))

    for n in random_list:
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return even_sum - odd_sum


def test_diff_odd_even():
    assert diff_odd_even(1, 0, 0) == 0, 'Result is invalid for params for 1, 0, 0.'
    assert diff_odd_even(6, 2, 2) == 12, 'Result is invalid for params for 6, 2, 2.'


def main():
    num_limit = int(input('Enter amount of numbers to generate: '))
    lower_bound = int(input('Enter lower bound: '))
    upper_bound = int(input('Enter upper bound: '))
    res = diff_odd_even(num_limit, lower_bound, upper_bound)
    print(f'The difference between even and odd sum of random numbers is {res}')


main()



