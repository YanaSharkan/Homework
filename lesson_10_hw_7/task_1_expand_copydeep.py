"""
This module has a function that create deep copy of a list, dict, tuple.
"""

original_list = [1, 2, ['a']]
my_dict = {'a': 2, 3: 'b', 'c': [1, 2.3]}


def copydeep(value):
    if isinstance(value, list) or isinstance(value, tuple):
        list_copy = []
        for el in value:
            list_copy.append(copydeep(el))
        if isinstance(value, tuple):
            return tuple(list_copy)
        return list_copy
    elif isinstance(value, dict):
        dict_copy = {}
        for key in value:
            dict_copy[key] = copydeep(value[key])
        return dict_copy

    return value



def test_copydeep():
    test_list = [1, 2, ['a', ['b']], {'a': 2, 3: 'b', 'c': [2.3]}, (1, 3)]
    copy_list = copydeep(test_list)
    assert copy_list is not test_list, 'List should be a copy.'
    assert copy_list[2] is not test_list[2], 'Inner list should be a copy.'
    assert copy_list[2][1] is not test_list[2][1], 'Second level of list should be a copy.'
    assert copy_list[2][1][0] is test_list[2][1][0], 'Index [2][1][0] should be a copy.'
    test_list.append([2])
    assert len(copy_list) != len(test_list)
    assert copy_list[3].get('c')[0] == 2.3, 'copy_list[3][\'c\'][0] should be 2.3.'
    assert copy_list[4][1] == 3, 'copy_list[4][1] should be 3.'
    assert copy_list[4] is not test_list[4], 'Nested tuple should be a copy.'


def main():
    test_copydeep()
    print('Test passed')


if __name__ == '__main__':
    main()





