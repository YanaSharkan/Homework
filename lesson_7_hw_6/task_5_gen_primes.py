"""
In this module function generates all prime numbers from 1
to 100 as a list.
"""


def gen_primes(max_num=100):
    factors = [2, 3, 5, 7]
    numbers = [elem for elem in factors if elem <= max_num]
    for i in range(7, max_num, 2):
        if i not in factors and len([j for j in factors if i % j == 0]) == 0:
            numbers.append(i)

    return numbers


def test_gen_primes():
    primes = gen_primes()
    assert len(primes) == 25, 'Amount of prime numbers in range 1 to 100 should be 25.'
    assert primes[0] == 2, 'First element should be 2.'
    assert primes[-1] == 97, 'Last element should be 97.'


def main():
    test_gen_primes()
    max_number = int(input('Enter amount of numbers: '))
    print(f'List of prime numbers is {gen_primes(max_number)}')


main()
