import sys
import re

# open file, read it, strip whitespaces
file = open(file=sys.argv[1]).read().strip()


# def make_list_of_numbers_from_string(string):
#     digit_i = []
#     trigger = True
#     while trigger is True:
#         for i, ch in enumerate(string):
#             if ch.isdigit():
#                 print(f'found digit {ch} at {i} position')
#                 digit_i.append(i)
#             else:
#                 print('found non-digit')
#                 trigger = False
#     all_numbers = string[digit_i]
#     return(all_numbers)

def prepare_cards_into_list_of_numbers(card):
    s = card.strip()
    digits = re.findall(r'\d+', s) # find digit (\d) 1 or more times (+)
    return(digits)


game_score = []
for line in file.split('\n'):
    print(line) #
    id, cards = line.split(':')
    winning_card, my_card = cards.split('|')
    winning_card, my_card = prepare_cards_into_list_of_numbers(winning_card), prepare_cards_into_list_of_numbers(my_card)
    print(f"winning_card is {winning_card}, \n my_card is {my_card}") #
    


# if __name == main():