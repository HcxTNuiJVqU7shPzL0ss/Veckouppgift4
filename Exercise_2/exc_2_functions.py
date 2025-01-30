#####################################################################
# Jan Berglund - exc_2_functions.py
#
# Veckouppgift 4
# Vecka 5, 27/1
#
#####################################################################


# 2.1
def string_print(input_name):
    print(f'{input_name} is a programing whizz!')

# 2.2a
def eko(input_string):
    print(f'{input_string}{input_string}')


# 2.2b
def eko_cnt(input_string, cnt):
    print_string = ''
    while cnt > 0:
        print_string += input_string
        cnt -= 1
    print(print_string)


# 3
def loop3():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
    print(y)


# 4
def last(param_list):
    return param_list[-1]


# 5
def cut_edges(input_list):
    # From elemet 1, up to but not including last element
    ret_list = input_list[1:-1]
    return ret_list


# 6
def increase(x):
    x += 1
    return x


#7
def average(x, y):
    avg = ((x + y) / 2)
    return avg


# 8
def check_sort_list(list_in):
    x = 0
    if len(list_in) == 0:
        print('\nThe list is empty!')
    else:
        print('\nThe list has', len(list_in), 'elements:')
        for i in list_in:
            x += 1
            print(str(x) + '. ' + str(i))


def gogo():
    input('\nPress Enter to continue')


# End it all
def endend():
    input('\n\nPress Enter to finish!')
