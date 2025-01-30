#####################################################################
# Jan Berglund - main.py
#
# Veckouppgift 4
# Vecka 5, 27/1
#
# 2 Öva på funktioner och moduler
#####################################################################


from exc_2_functions import string_print

from exc_2_functions import eko

from exc_2_functions import eko_cnt

from exc_2_functions import loop3

from exc_2_functions import last

from exc_2_functions import cut_edges

from exc_2_functions import increase

from exc_2_functions import average

from exc_2_functions import check_sort_list

from exc_2_functions import gogo, endend


# 2.1
gogo()
print('\nExc 2.1')
string_print('Jan')


# 2.2a
gogo()
print('\nExc 2.2a')
eko('hej')


# 2.2b
gogo()
print('\nExc 2.2b')
eko_cnt('hej', 4)


# 3
gogo()
print('\nExc 2.3')
loop3()


# 4
gogo()
print('\nExc 2.4')
last_list = [1, 2, 3]
print(last(last_list))


# 5
gogo()
print('\nExc 2.5')
slice_list = [1, 2, 3, 4]
cut_list = cut_edges(slice_list)
print(cut_list)


# 6
gogo()
print('\nExc 2.6')
number_inc = 4
print(increase(number_inc))


# 7
gogo()
print('\nExc 2.7')
x_no = 4
y_no = 8
print(average(x_no, y_no))


# 8
gogo()
print('\nExc 2.8')
list_in_empty = []
list_in_2 = ['a', 'b', 3.14]
check_sort_list(list_in_empty)
check_sort_list(list_in_2)


endend()
