"""
This module returns a list of all surnames from the file.
"""


class NotReadableFileException(Exception):
    """
    Exception raised for errors if the file is not readable.
    """
    def __init__(self, message='File is not readable!'):
        self.message = message
        super().__init__(self.message)


def read_info(file_name):
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        surnames = []
        file.close()
    except Exception:
        raise NotReadableFileException()
    for line in lines:
        parsed_line = line.split('\t')
        if len(parsed_line) > 2:
            surnames.append(parsed_line[1])
    return surnames


def main():
    file_name = input('Enter name of file (default name of file '
                      'is \'names.txt\') : ')
    if not file_name:
        file_name = 'names.txt'
    try:
        surnames = read_info(file_name)
        print(f'Surnames: {surnames}')
    except NotReadableFileException as err:
        print(err.message)


if __name__ == '__main__':
    main()
