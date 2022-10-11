"""
Reads domains from file, presents them as list.
"""


class NotReadableFileException(Exception):
    """
    Exception raised for errors if the file is not readable.
    """
    def __init__(self, message='File is not readable!'):
        self.message = message
        super().__init__(self.message)


def read_domains(file_name):
    try:
        file = open(file_name, "r")
        domains = file.readlines()
        file.close()
    except Exception:
        raise NotReadableFileException()
    return list(map(lambda d: d.replace('.', '').replace('\n', ''), domains))


def main():
    files_name = input('Enter name of file (default name of file '
                       'is \'domains.txt\') : ')
    if not files_name:
        file_name = 'domains.txt'
    try:
        domains = read_domains(file_name)
        print(f'Domains: {domains}')
    except NotReadableFileException as err:
        print(err.message)


if __name__ == '__main__':
    main()
