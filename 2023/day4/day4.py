
import sys
# open file, read it, strip whitespaces
file = open(file=sys.argv[1]).read().strip()

game_score = []
for line in file.split('\n'):
    print(line) #
    id, cards = line.split(':')
    winning_card, my_card = cards.split('|')
    print(f"winning_card is {winning_card}, \n my_card is {my_card}") #
    print(list(my_card))
    




# if __name == main():