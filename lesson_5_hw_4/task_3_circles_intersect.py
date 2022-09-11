"""
This module calculates if circles intersect.
"""


import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)  # Distance between centres.
    if d <= r1 - r2 or d <= r2 - r1:  # One circle is inside another, don't intersect.
        return False
    elif d > r1 + r2:  # Don't intersect.
        return False
    else:
        return True


def test_circles_intersect():
    assert circles_intersect(1, 1, 2, 4, 4, 1) is False, 'Invalid result for (1, 1, 2, 4, 4, 1).'
    assert circles_intersect(1, 1, 2, 3, 3, 1) is True, 'Invalid result for (1, 1, 2, 3, 3, 1).'


def main():
    test_circles_intersect()
    circle_1 = input('Please enter params with a comma for the first circle x1,y1,r1:').split(',')
    params_circle_1 = [int(p) for p in circle_1]
    circle_2 = input('Please enter params with a comma for the second circle x2,y2,r2:').split(',')
    params_circle_2 = [int(p) for p in circle_2]

    res = circles_intersect(*params_circle_1, *params_circle_2)
    print(res)


main()
