import math
a = 1
b = 5
c = 4

x1 = (-b + math.sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)
x2 = (-b - math.sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)

print('Value of expression x1 is {}'.format(x1))
# -1.0

print('Value of expression x2 is {}'.format(x2))
# -4.0
