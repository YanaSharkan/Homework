"""
Function in this module checks if the given point is inside the circle
and returns the corresponding boolean value.
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def check_is_inside(self, point: Point):
        d = math.sqrt((point.x - self.center_x) ** 2 +
                      (point.y - self.center_y) ** 2)
        return d <= self.radius


def test_check_is_inside():
    circle = Circle(1, 1, 3)
    point = Point(-1, -1)
    point_2 = Point(-2.1, -2.1)
    assert circle.check_is_inside(point) is True, \
        'Invalid result for params Point(-1, -1), Circle(1, 1, 3)'
    assert circle.check_is_inside(point_2) is False, \
        'Invalid result for params Point(-2.1, -2.1), Circle(1, 1, 3)'


def main():
    test_check_is_inside()
    print('Test passed!')


if __name__ == '__main__':
    main()
