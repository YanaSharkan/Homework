import math


def degrees_2_radians(degrees):
    radians = degrees * math.pi / 180
    cosine = round(math.cos(radians), 3)
    return cosine


print('The value of cosine of angle {0} is: {1}'.format(60, degrees_2_radians(60)))
print('The value of cosine of angle {0} is: {1}'.format(45, degrees_2_radians(45)))
print('The value of cosine of angle {0} is: {1}'.format(40, degrees_2_radians(40)))
