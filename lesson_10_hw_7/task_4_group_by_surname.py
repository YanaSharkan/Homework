"""
Function in this module counts amount of students in which
group by their first letter of surname. There are groups: "A-I", "J-P", "Q-T", "U-Z".
"""

from string import ascii_uppercase


def group_by_surname(list_of_enrollees):
    groups = {'A-I': 0,
              'J-P': 0,
              'Q-T': 0,
              'U-Z': 0,
              }
    for enrollee in list_of_enrollees:
        first_last_name = enrollee.strip().split(' ')
        if len(first_last_name) >= 2:
            surname = first_last_name[1][0]
            if surname in ascii_uppercase[0:9]:
                groups['A-I'] += 1
            elif surname in ascii_uppercase[9:16]:
                groups['J-P'] += 1
            elif surname in ascii_uppercase[16:20]:
                groups['Q-T'] += 1
            elif surname in ascii_uppercase[16:25]:
                groups['U-Z'] += 1

    return groups

def test_group_by_surname():
    list_of_names = ['Name Asurname', 'Name Nsurname', 'Name', 'Name 1']
    assert group_by_surname(list_of_names)['A-I'] == 1, 'Invalid result for Name Asurname'
    assert group_by_surname(list_of_names)['J-P'] == 1, 'Invalid result for Name Nsurname'
    assert group_by_surname(list_of_names)['Q-T'] == 0, 'Invalid result for Q-T'
    assert group_by_surname(list_of_names)['U-Z'] == 0, 'Invalid result for U-Z'



def main():
    test_group_by_surname()
    enrollees = input('Enter name and surname of enrollees: ')
    list_of_enrolees = enrollees.split(',')
    print(group_by_surname(list_of_enrolees))


if __name__ == '__main__':
    main()