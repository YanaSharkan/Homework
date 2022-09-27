"""
Function in this module shuffles sentence with leaving it readable.
"""


from random import randint, shuffle


def shuffle_string(string):
    while True:
        symbols_list = list(string)
        shuffle(symbols_list)
        result = ''.join(symbols_list)

        if result != string:
            return result


def shuffle_word(word):
    if len(word) < 4 or word.isalpha() is False:
        return word
    else:
        inner_letters = word[1: -1]
        list_of_parts = [inner_letters[i:i + 3] for i in range(0, len(inner_letters), 3)]

        for i, part in enumerate(list_of_parts):
            if len(part) > 1:
                list_of_parts[i] = shuffle_string(part)

        return word[0] + ''.join(list_of_parts) + word[-1]


def permutuate(text):
    words = text.split(' ')
    for i, word in enumerate(words):
        words[i] = shuffle_word(word)

    return ' '.join(words)


def main():
    sentence = input('Enter sentence: ')
    shuffled_sentence = permutuate(sentence)
    print(f'Original text is: {sentence}')
    print(f'Shuffled text is: {shuffled_sentence}')


main()
