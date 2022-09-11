"""
This module solves quadratic equation in complex and non-complex numbers.
"""


import math
import cmath


def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant != 0:
        x_1 = (-b + math.sqrt(discriminant)) / 2*a
        x_2 = (-b - math.sqrt(discriminant)) / 2*a
        return x_1, x_2
    else:
        return - (b / 2*a), None


def solve_quadratic_equation_complex(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant != 0:
        x_1 = (-b + cmath.sqrt(discriminant)) / 2*a
        x_2 = (-b - cmath.sqrt(discriminant)) / 2*a
        return x_1, x_2
    else:
        return - (b / 2*a), None


def test_solve_quadratic_equation_no_roots():
    x_1, x_2 = solve_quadratic_equation(2, 2, 2)
    assert x_1 is None, 'Root one for (2, 2, 2) is wrong'
    assert x_2 is None, 'Root two for (2, 2, 2) is wrong'


def test_solve_quadratic_equation_one_root():
    x_1, x_2 = solve_quadratic_equation(2, 4, 2)
    assert x_1 == -4, 'Root one for (2, 4, 2) is wrong'
    assert x_2 is None, 'Root two for (2, 4, 2) is wrong'


def test_solve_quadratic_equation_two_roots():
    x_1, x_2 = solve_quadratic_equation(3, 4, 1)
    assert x_1 == -3.0, 'Root one for (3, 4, 1) is wrong'
    assert x_2 == -9.0, 'Root two for (3, 4, 1) is wrong'


def test_solve_quadratic_equation_complex():
    c_x_1, c_x_2 = solve_quadratic_equation_complex(2, 2, 2)
    assert c_x_1 == -2+3.4641016151377544j, 'Root one for (2, 2, 2) is wrong'
    assert c_x_2 == -2-3.4641016151377544j, 'Root two for (2, 2, 2) is wrong'
    c_x_1, c_x_2 = solve_quadratic_equation_complex(1, 5, 6)
    assert c_x_1 == -2+0j, 'Root one for (1, 5, 6) is wrong'
    assert c_x_2 == -3+0j, 'Root two or (1, 5, 6) is wrong'


def main():
    test_solve_quadratic_equation_no_roots()
    test_solve_quadratic_equation_one_root()
    test_solve_quadratic_equation_two_roots()
    test_solve_quadratic_equation_complex()

    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = int(input('Enter c:'))

    x_1, x_2 = solve_quadratic_equation(a, b, c)
    print(f'Root 1: {x_1}, root 2: {x_2}')

    c_x_1, c_x_2 = solve_quadratic_equation_complex(a, b, c)
    print(f'Root 1 complex: {c_x_1}, root 2 complex: {c_x_2}')


main()



