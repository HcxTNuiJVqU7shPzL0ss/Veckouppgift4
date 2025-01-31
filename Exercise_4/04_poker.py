

import random


# Random card from deck
# 11 = Jack, 12 = Queen, 13 = King, 14 = Ace
def rand_card():
    value_def = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    color_def = ['hearts', 'clubs', 'diamonds', 'spades']
    card_value = random.sample(value_def, 1)[0] # Randomly pick one, "first element"
    card_color = random.sample(color_def, 1)[0]
    return [card_color, card_value]


# Check any occurrences of "same numbers"
# in hand
# Find 4 and 3 of a kind, full house, 2 or 1 pair
def check_equal(hand_in):
    one_pair = False
    two_pairs = False
    three_of = False
    full_house = False
    four_of = False
    nothing = False

    your_equals = ''


    # Used for testing only
    # hand_in = [['spades', 4], ['clubs', 4], ['hearts', 4], ['diamonds', 4], ['diamonds', 4]] # 5 (fail)
    # hand_in = [['spades', 4], ['clubs', 4], ['hearts', 4], ['diamonds', 4], ['diamonds', 3]] # 4
    hand_in = [['spades', 4], ['clubs', 4], ['hearts', 4], ['diamonds', 3], ['diamonds', 3]] # Full House
    # hand_in = [['spades', 4], ['clubs', 4], ['hearts', 4], ['diamonds', 3], ['diamonds', 2]] # 3
    # hand_in = [['spades', 4], ['clubs', 4], ['hearts', 3], ['diamonds', 3], ['diamonds', 2]] # 2 pair
    # hand_in = [['spades', 4], ['clubs', 4], ['hearts', 3], ['diamonds', 2], ['diamonds', 14]] # 1 pair
    # hand_in = [['spades', 8], ['clubs', 6], ['hearts', 4], ['diamonds', 3], ['diamonds', 2]] # Nada


    cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]       # Count equals

    # List with only the numbers, not the suit
    card_numbers = [x[1] for x in hand_in]

    for numb in range(2,15,1):
        cnt[numb] = card_numbers.count(numb)    # Count how many

    print(cnt)

    max_cnt = max(cnt)              # Max number of equal values
    idx_max = cnt.index(max_cnt)    # Index of first max value

    idx_2 = 0                       # Used if more than one to care about

    if max_cnt > 4:
        print('Something crashed!') # Not playing with wild cards
        your_equals = 'No wild cards allowed!'
        quit()
    elif max_cnt == 4:              # 4 of the same value
        your_equals = 'You have 4 of a kind'
        four_of = True
    elif max_cnt == 3:              # 3 of, or Full House
        if cnt.count(2) == 1:       # + 1 pair == Full House
            idx_2 = cnt.index(2)
            your_equals = 'You have a Full House, 3 of: ' + str(idx_max) +\
                          ' , and 2 of: '+ str(idx_2)
            full_house = True
        else:                       # 3 of the same value
            your_equals = 'You have 3 of a kind'
            three_of = True
    elif max_cnt == 2:              # 2 pairs
        if cnt.count(2) == 2:
            your_equals = 'You have 2 pairs'
            two_pairs = True
        else:                       # 1 pair
            your_equals = 'You have 1 pair'
            one_pair = True
    else:
        your_equals = 'you have no equal cards'
        nothing = True              # No equal values


    print(your_equals)

    print(f'Max: {max_cnt} at index {idx_max}')
    print(f'4: {four_of}, FH: {full_house}, 3: {three_of}, 2: {two_pairs}, '
          f'1: {one_pair}, no: {nothing}, your hand: {your_equals}')



# Collect the 5 cards in a hand
hand = []

# Card 1
while True:
    card_1 = rand_card()
    if card_1 not in hand:
        hand.append(card_1)
        break
    else:
        continue

# Card 2
while True:
    card_2 = rand_card()
    if card_2 not in hand:
        hand.append(card_2)
        break
    else:
        continue

# Card 3
while True:
    card_3 = rand_card()
    if card_3 not in hand:
        hand.append(card_3)
        break
    else:
        continue

# Card 4
while True:
    card_4 = rand_card()
    if card_4 not in hand:
        hand.append(card_4)
        break
    else:
        continue

# Card 5
while True:
    card_5 = rand_card()
    if card_5 not in hand:
        hand.append(card_5)
        break
    else:
        continue

check_equal(hand)

#print(hand)
