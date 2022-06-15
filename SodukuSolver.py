# from tabulate import tabulate
def print_separating_row():
    print('+ — ' * 9, end='+ \n')
    return 

def print_grid(x:list):
    print('')
    for row in x:
        print_separating_row()
        print('| ', end='')
        print(*row, sep=' | ', end=' |\n')
    print_separating_row()
    return

def allotcate_placeholder_data(grid:list):
    for _ in range(9):
        grid.append([])
        for _ in range(9):
            grid[-1].append('0')
    return 

def ask_and_allocate(grid:list) -> list:
    output = grid[:]
    for row_index, row in enumerate(grid):
        for index, element in enumerate(row):
            num = '-1'
            while int(num) < 0 or int(num) > 9:
                num = input('Input your row '+ str(row_index+1) +' slot ' + str(index+1) + ' value:' )
                while not num.isdigit():
                    num = input('Input your row '+ str(row_index+1) +' slot ' + str(index+1) + ' value:' )
            output[row_index][index] = num
    return output

def solve(soduku: list) -> list:
    # solves all the values in soudku and returns the result out
    # calls a function on placeholder locations to analyse all the possible values the specific slot can be (coordinates: list, soduku: list) -> (possible_values: list)
        # function to analyse a row/column of elements to suggest possible values () 
    # calls a function to scan all the possible_values list for a suitable value for one slot and returns the corrected soduku  (possible_values: list, soduku: list) -> ( coordinates: list, soduku: list)
    # calls a function to update possible_values list (possible_values: list, coordinates: list) -> (possible_values: list)
    # calls a function to check for any 0s in the soduku (soduku: list) -> (complete: bool)
    return 


def check_validity(soduku: list) -> bool:
    # checkd whether there is a unique solution or not
    return 

soduku = []
allotcate_placeholder_data(soduku)
ask_and_allocate(soduku)

print_grid(soduku)
