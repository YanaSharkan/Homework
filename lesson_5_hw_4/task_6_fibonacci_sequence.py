"""
This module calculates Nth number from Fibonacci sequence.
"""


def fibonacci_num(num):
    """
    Function returns Fibonacci number for user readable index (indexing starts from 1).
    """
    n = num - 1
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return n
    return fibonacci_num(num - 1) + fibonacci_num(num - 2)


def test_fibonacci_num():
    assert fibonacci_num(10) == 34, 'Invalid return number for 100.'
    assert fibonacci_num(1) == 0, 'Invalid return number for 1.'
    assert fibonacci_num(5) == 3, 'Invalid return number for 5.'


def main():
    test_fibonacci_num()
    num = int(input('Please enter number:'))
    if num > 49:  # Check max number
        print('Number should be less then 50')
    else:
        fib_for_num = fibonacci_num(num)
        print(f'Fibonacci number for number {num} is {fib_for_num}.')
    print(f'Fibonacci number for number 20 is {fibonacci_num(20)}')


main()







# nterms = int(input('How many terms?'))
#
# n1, n2 = 0, 1
# count = 0

# if nterms <= 0:
#     print('Pos int')
# elif nterms == 1:
#     print('Fib ', nterms, ':')
#     print(n1)
# else:
#     print('Fib sec')
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

