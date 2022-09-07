rest_args = [1, 2, 3, 4, 5]
start_arg = 3


def my_sum(*args, start=0):
    total_sum = sum(args, start)
    return total_sum


total = my_sum(*rest_args, start_arg)
print('Sum for args {0} and start {1} is {2}'.format(rest_args, start_arg, total))