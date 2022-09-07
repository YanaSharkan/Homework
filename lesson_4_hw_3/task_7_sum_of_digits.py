numbers_input = input('Enter tne number: ')


def sum_digits(numbers):
    total = 0
    for n in numbers:
        total += (ord(n) - 48)
    return total


res = sum_digits(numbers_input)
print('Total sum of digits: {}'.format(res))
