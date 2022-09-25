"""
In this module function generates all prime numbers from 1
to 100 as a list.
"""


def gen_primes():
    numbers = []
    factors = [2, 3, 5, 7]
    for i in range(2, 100):
        if i in factors or len([j for j in factors if i % j == 0]) == 0:
            numbers.append(i)

    return numbers


def test_gen_primes():
    primes = gen_primes()
    assert len(primes) == 25, 'Amount of prime numbers in range 1 to 100 should be 25.'
    assert primes[0] == 2, 'First element should be 2.'
    assert primes[-1] == 97, 'Last element should be 97.'


def main():
    test_gen_primes()
    print(f'List of prime numbers is {gen_primes()}')


main()
