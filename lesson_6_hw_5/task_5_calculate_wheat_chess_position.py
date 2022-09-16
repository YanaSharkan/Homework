"""
This program calculates starting from which cell of the board it is necessary to give Nkg of grain,
where N is entered by the user.
"""


def calculate_wheat_chess_position(kilograms):
    letters = 'abcdefgh'
    for i in range(0, 8):
        for j in range(0, 8):
            number_of_seeds = pow(2, i*8 + j)
            if number_of_seeds * 0.000035 >= kilograms:
                return letters[i] + str(j + 1)

    return None


def test_calculate_wheat_chess_position():
    assert calculate_wheat_chess_position(0.03584) == 'b3', 'Invalid result for 0.03584 kg.'
    assert calculate_wheat_chess_position(1) == 'b8', 'Invalid result for 1 kg.'
    assert calculate_wheat_chess_position(0.000035) == 'a1', 'Invalid result for 35 mg.'


def main():
    test_calculate_wheat_chess_position()
    kilograms = float(input('Enter quantity of kg: '))
    res = calculate_wheat_chess_position(kilograms)
    print(f'Index of cell: {res}')


main()