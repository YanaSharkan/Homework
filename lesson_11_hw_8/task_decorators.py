"""This module contains decorator, which checks return type of function
and throws an exception."""

import functools


class UnexpectedTypeException(Exception):
    """
    Exception raised for errors if we find unexpected type.
    """
    def __init__(self, message='Unexpected type'):
        self.message = message
        super().__init__(self.message)


def expected(expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_res = func(*args, **kwargs)
            if not isinstance(func_res, expected_types):
                raise UnexpectedTypeException()

            return func_res
        return wrapper
    return decorator


@expected((int, dict))
def test_expected_int():
    return '1'  # Return value forces decorator to raise exception


@expected((dict,))
def test_expected_dict():
    return ['1']  # Return value forces decorator to raise exception


@expected((int,))
def test_expected_return(a, b):
    return a*b


def test_expected_decorator():
    try:
        test_expected_int()
        assert 2 == 1, 'Exception was not raised for int.'
    except UnexpectedTypeException as error:
        assert error.message == 'Unexpected type', 'Type assertion failed for int.'

    try:
        test_expected_dict()
        assert 2 == 1, 'Exception was not raised for dict.'
    except UnexpectedTypeException as error:
        assert error.message == 'Unexpected type', 'Type assertion failed for dict.'

    assert test_expected_return(2, 3) == 6, 'Type assertion did not return function result.'


def main():
    test_expected_decorator()
    print(f'Test passed!')


if __name__ == '__main__':
    main()
