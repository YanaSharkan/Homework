import math

r = int(input('Enter radius: '))
h = int(input('Enter height: '))


def cone_square_and_volume(radius, height):
    s = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))
    v = (math.pi * radius**2 * height) / 3
    return s, v


square, volume = cone_square_and_volume(r, h)
print('Cone\'s square is equal : {0}, volume {1}'.format(round(square, 2), round(volume, 2)))