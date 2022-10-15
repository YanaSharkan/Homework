"""
This module provide class Godzilla.
"""


class Godzilla:
    def __init__(self, volume):
        self.volume = volume
        self.filled_stomach = 0

    def eat_people(self, volume_person):
        if self.is_hungry():
            self.filled_stomach += volume_person

    def is_hungry(self):
        return self.filled_stomach / self.volume < 0.9


def main():
    v_of_stomach = int(input('Enter a volume of stomach: '))
    godzilla = Godzilla(v_of_stomach)
    while godzilla.is_hungry():
        person = int(input('Enter volume of person: '))
        godzilla.eat_people(person)
    print('Godzilla is not hungry!')


if __name__ == '__main__':
    main()
