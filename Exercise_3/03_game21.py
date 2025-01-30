#####################################################################
# Jan Berglund - 03_game21.py
#
# Veckouppgift 4
# Vecka 5, 27/1
#
# "3" Spelet 21
#####################################################################


import random


def gogo():
    input('\nPress Enter to continue')


# End it all
def endend():
    input('\n\nPress Enter to finish!')


def find_bust():
    card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    series = 0
    last_card = 0
    list_used = []
    for card in card_list:
        series += card
        list_used.append(card)
        if series > 21:
            last_card = card
            break
    print('\nThe number in the series higher then 21 is: ' + str(series)
          + '.\nThe last number added was: ' + str(last_card) + '.')
    print('The list used was:', list_used)


def rand_bust():
    series_rand = 0
    last_card_rand = 0
    rand_used = []
    while series_rand < 21:
        rand_card = random.randint(1, 13)
        last_card_rand = rand_card
        series_rand += rand_card
        rand_used.append(rand_card)
    print('\nThe number in the rando higher then 21 is: ' + str(series_rand)
          + '.\nThe last number added was: ' + str(last_card_rand) + '.')
    print('The list used was:', rand_used)


# Version 1
gogo()
print('\nVersion 1')
find_bust()


# Version 2
gogo()
print('\nVersion 2')
rand_bust()


endend()
