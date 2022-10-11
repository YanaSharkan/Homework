"""
This module parses and changes dates to new format.
"""

from datetime import datetime


def format_date(date_str):
    date_original = date_str.replace('1st', '1').replace('th', '')\
        .replace('rd', '').replace('nd', '')
    date_parsed = datetime.strptime(date_original, '%d %B %Y')
    return datetime.strftime(date_parsed, '%d/%m/%Y')


def format_dates(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        dates = []
        for line in lines:
            parsed_line = line.split(' - ')
            if len(parsed_line) > 1:
                date_original = parsed_line[0]
                date_modified = format_date(date_original)
                dates.append(
                    {
                        'date_original': date_original,
                        'date_modified': date_modified
                    }
                )
        return dates


def main():
    file_name = input('Enter name of file (default name of file '
                      'is \'authors.txt\') : ')
    if not file_name:
        file_name = 'authors.txt'
    try:
        dates = format_dates(file_name)
        print(f'Modified data: {dates}')
    except OSError:
        print('Could not read file!')


if __name__ == '__main__':
    main()
