red = 12
green = 13
blue = 14

def get_integer(string):
    return int(''.join(list(filter(str.isdigit, string))))

def check_game(game):
    #split each handful
    handfuls = game.split(';')
    #split handful
    for hand in handfuls:
        for color in hand.split(','):
            digit = get_integer(color)
            if "red" in color and digit > red:
                return False
            if "blue" in color and digit > blue:
                return False
            if "green" in color and digit > green:
                return False
    return True

def check_game_for_minumum_blocks(game):
    #split each handful
    handfuls = game.split(';')
    max_blocks = {'red' : 0, 'green' : 0, 'blue' : 0}
    #split handful
    for hand in handfuls:
        for color in hand.split(','):
            digit = get_integer(color)
            max_blocks['red'] = digit if "red" in color and digit > max_blocks['red'] else max_blocks['red']
            max_blocks['blue'] = digit if "blue" in color and digit > max_blocks['blue'] else max_blocks['blue']
            max_blocks['green'] = digit if "green" in color and digit > max_blocks['green'] else max_blocks['green']            
    print(max_blocks)
    return max_blocks
if __name__ == "__main__":
    ids = []
    all_answers = []
    with open("game.txt") as games:
        gg = 0
        for game in games:
            id, handfuls = game.split(":")
            id = get_integer(id)
            if check_game(handfuls):
                gg += 1
                ids.append(id)
            m = check_game_for_minumum_blocks(handfuls)
            # create a variable to store result
            answer = 1
            # run a loop
            for value in m.values():
                answer = answer*value
            all_answers.append(answer)
            print(sum(all_answers))
        # print(sum)