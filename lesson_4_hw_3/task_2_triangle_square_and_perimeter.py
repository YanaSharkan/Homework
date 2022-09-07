import math

cathetus_1 = int(input('Enter first cathetus: '))
cathetus_2 = int(input('Enter second cathetus: '))


def triangle_square_and_perimeter(a, b):
    s = round((a * b / 2), 3)
    p = round((math.sqrt(a**2 + b**2) + a + b), 3)
    return s, p


square, perimeter = triangle_square_and_perimeter(cathetus_1, cathetus_2)
print('Triangle\'s square is equal : {0}, perimeter {1}'.format(square, perimeter))
