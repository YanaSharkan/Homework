entered_string = input('Please enter the string: ')


def string_operations(text):
    third_symbol = text[2]
    print('Third symbol of this string: {}'.format(third_symbol))
    penultimate = text[-2]
    print('Penultimate character of this string: {}'.format(penultimate))
    first_five = text[:5]
    print('First five characters of this string: {}'.format(first_five))
    without_last_two = text[:-2]
    print('The entire string except the last two characters: {}'.format(without_last_two))
    even_indices = text[::2]
    print('All characters with even indices (assuming that indexing starts at 0,'
          ' so characters are output starting from the first one).: {}'.format(even_indices))
    odd_indices = text[1::2]
    print('All characters with odd indices, that is,'
          ' starting from the second character of the string.: {}'.format(odd_indices))
    reverse_order = text[::-1]
    print('All characters in reverse order.: {}'.format(reverse_order))
    reverse_from_last_one = text[-1::-2]
    print('All the characters of the string one by one in reverse order,'
          ' starting with the last one.: {}'.format(reverse_from_last_one))
    length_of_the_string = len(text)
    print('The length of this string.: {}'.format(length_of_the_string))


string_operations(entered_string)

