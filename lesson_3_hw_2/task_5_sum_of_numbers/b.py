numbers = int(input('Enter tne number: '))
total = 0

while numbers > 0:
    i = numbers % 10
    total = total + i
    numbers = numbers // 10

print('Total sum of digits: {}'.format(total))

