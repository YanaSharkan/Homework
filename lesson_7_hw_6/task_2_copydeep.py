"""
This module has a function that create deep copy of a list.
"""

original_list = [1, 2, ['a']]


def copydeep(lst):
    list_copy = []
    for el in lst:
        if not isinstance(el, list):
            list_copy.append(el)
        else:
            list_copy.append(copydeep(el))
    return list_copy


def test_copydeep():
    test_list = [1, 2, ['a', ['b']]]
    copy_list = copydeep(test_list)
    assert copy_list is not test_list, 'List should be a copy.'
    assert copy_list[2] is not test_list[2], 'Inner list should be a copy.'
    assert copy_list[2][1] is not test_list[2][1], 'Second level of list should be a copy.'
    assert copy_list[2][1][0] is test_list[2][1][0], 'Index [2][1][0] should be a copy.'
    test_list.append([2])
    assert len(copy_list) != len(test_list)


def main():
    test_copydeep()
    print('Test passed')


main()
