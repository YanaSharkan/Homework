"""
Function in this module shuffles sentence with leaving it readable.
"""


from random import randint


def shuffle_string(string):
    result = string
    for i in range(0, len(string)):
        letter_index = randint(0, len(string) - 1)
        if letter_index != i:
            prev_result = result
            result = result[0:i] + result[letter_index] + result[i + 1:]
            result = result[0:letter_index] + prev_result[i] + result[letter_index + 1:]

    return result


def shuffle_word(word):
    if len(word) < 5 or word.isalpha() is False:
        return word
    else:
        inner_letters = word[1: -1]
        list_of_parts = [inner_letters[i:i + 3] for i in range(0, len(inner_letters), 3)]
        for part in list_of_parts:
            if len(part) > 2:
                word = word.replace(part, shuffle_string(part), 1)

        return word


def permutuate(text):
    words = text.split(' ')
    for word in words:
        text = text.replace(word, shuffle_word(word), 1)

    return text


def main():
    sentence = input('Enter sentence: ')
    shuffled_sentence = permutuate(sentence)
    print(f'Original text is: {sentence}')
    print(f'Shuffled text is: {shuffled_sentence}')


main()
