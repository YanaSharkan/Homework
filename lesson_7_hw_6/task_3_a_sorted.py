"""
In this module function gets copy of list with function sorted.
Copy sorted by element number value.
"""


def sort_list(lst):
    return sorted(lst, key=lambda x: float(x))


def test_sort_list():
    origin_list = [5, '9', 0, '452', 6.5, '6', 1, 2]
    sorted_list = sort_list(origin_list)
    assert sorted_list[5] == 6.5, 'Element with index 5 is not valid'
    assert sorted_list[0] == 0, 'Element with index 0 is not valid'
    assert sorted_list[7] == '452', 'Element with index 7 is not valid'


def main():
    test_sort_list()
    print('Tests passed')


main()
