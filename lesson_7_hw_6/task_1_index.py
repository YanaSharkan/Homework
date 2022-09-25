"""
In this module function returns index of the element of the list or
None if the element is not present.
"""


def index(lst, elem):
    for ind, element in enumerate(lst):
        if elem == element:
            return ind
    return None


def test_index():
    my_list = [1, 2, 'a', 2.3]
    assert index(my_list, 'a') == 2, f'Invalid return value with params {my_list}, \'a\').'
    assert index(my_list, 3) is None, f'Invalid return value with params {my_list}, 3).'


def main():
    test_index()
    print(f'Test passed')


main()
