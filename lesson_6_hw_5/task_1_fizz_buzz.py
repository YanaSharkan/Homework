"""
This module outputs numbers from 1 to 100 while replaces numbers,
that divisible by 3 and prints "Fizz",
by 5 and prints "Buzz", and by 3 and 5 prints "FizzBuzz."

"""


def output_numbers():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def main():
    output_numbers()


main()

