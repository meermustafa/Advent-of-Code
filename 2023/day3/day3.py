def find_symbol_idx(row, line):
    indices = set()
    for col, symbol in enumerate(line):
        if not symbol.isalnum() and symbol is not '.' and symbol is not '\n':
            print(f"symbol: {symbol}")
            indices.add((row, col))
    return indices
"""
def find_digit(row, col, grid):
    all_possible_number_positions = set()
    print(row, col)
    for i in range(-1, 1):
        for j in range(-1, 1):
            if grid[row+i][col+j].isdigit():
                all_possible_number_positions.add((row+i,col+j))
    for each digit that we found, find the full number associated and remove duplicates
        find_full_number()
def find_full_number(digit_row, digit_col, grid):
    
    for colIdx in range(digit_col, 0):
        if grid[digit_row][colIdx].isdigit():
"""
def calculate_stars(star_coords, grid):
    sum_of_products = 0
    for key, values in star_coords.items():
        if len(values) != 2:
            continue
        else:
            nums = extract_numbers(values, grid)
            product = 1
            for num in nums:
                product *= num
            sum_of_products += product
    print ("Sum of product" , sum_of_products)

        
def find_adjacent_symbol(grid):
    init_coordinates = None
    final_coordinates = None
    star_dict = dict()
    coords = set()
    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            col = row[j]
            if col.isdigit():
                init_coordinates = (i,j)
                print(f"init: {init_coordinates}")
                while col.isdigit():
                    j+=1
                    col = row[j]
                final_coordinates = (i, j-1)
                print(f"final: {final_coordinates}")
                
                for x in range(init_coordinates[0]-1, final_coordinates[0]+2):
                    for y in range(init_coordinates[1]-1, final_coordinates[1]+2):
                        print(f"x,y: {x,y}")
                        if x < 0 or y < 0 or x > len(grid)-1 or y > len(row)-1:   
                            continue
                        symbol = grid[x][y]
                        print(symbol)
                        if not symbol.isalnum() and symbol != '.' and symbol != '\n':
                                coords.add((init_coordinates, final_coordinates))
                                print(f"This coordinate {x,y} has a symbol adjacent")
                                if symbol == "*":
                                    if f"{x,y}" in star_dict.keys():
                                        star_dict[f"{x,y}"].append((init_coordinates, final_coordinates))
                                    else:
                                        star_dict[f"{x,y}"] = [(init_coordinates, final_coordinates)]
            j+=1
    print(coords)
    calculate_stars(star_dict, grid)
    print(len(coords))
    return coords

def extract_numbers(coordinates, grid):
    all_numbers_str = []
    for coords in coordinates:
        start, end = coords
        number = ''
        i = start[1]
        while i <= end[1]:
            number += grid[start[0]][i]
            i+=1
        all_numbers_str.append(number)
    
    all_numbers = [int(x) for x in all_numbers_str]
    return all_numbers
    

if __name__ == "__main__":
    internal_grid = []
    symbols = []
    with open("grid.txt") as grid:
        for row, line in enumerate(grid):
            internal_grid.append(line)
            symbols.extend(find_symbol_idx(row, line))
        coords = find_adjacent_symbol(internal_grid)
        print(extract_numbers(coords, internal_grid))
        