"""
In this module function gets copy of list with function sorted.
Copy sorted by first digit of number value.
"""


def sort_list(lst):
    return sorted(lst, key=lambda x: str(x)[0])


def test_sort_list():
    origin_list = [472, 326, 1, '1101000', 9, '20', 863, '0']
    sorted_list = sort_list(origin_list)
    assert sorted_list[0] == '0', 'Element with index [0] should be 0.'
    assert sorted_list[7] == 9, 'Element with index [7] should be 9.'


def main():
    test_sort_list()
    print('Tests passed!')


main()
