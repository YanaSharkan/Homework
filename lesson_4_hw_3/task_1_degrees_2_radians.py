import math


def degrees_2_radians(degrees):
    return degrees * math.pi / 180


params = [60, 45, 40]

for i in params:
    formatted_cos = round(math.cos(degrees_2_radians(i)), 3)
    print('The value of cosine of angle {0} is: {1}'.format(i, formatted_cos))

