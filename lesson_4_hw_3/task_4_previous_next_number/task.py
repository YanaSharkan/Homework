def read_and_return_text():
    number = int(input('    Please enter an integer number: '))
    next_num = number + 1
    previous_num = number - 1
    print('    Next number for number {0} is {1}.\n'
          '    Previous number for number {0} is {2}.'.format(number, next_num, previous_num))


read_and_return_text()


