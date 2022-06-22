# from tabulate import tabulate
def print_separating_row():
# print the separating row of the grid 
    print('+ — ' * 9, end='+ \n')
    return 

def print_grid(x:list):
# print grid in a clean way 
    print('')
    print('           ~ Sudoku Grid ~          ')
    for row in x:
        print_separating_row()
        print('| ', end='')
        print(*row, sep=' | ', end=' |\n')
    print_separating_row()
    return

def allotcate_placeholder_data(grid:list):
# set the 2d array grid and allowcate 0 as placeholder value
    for _ in range(9):
        grid.append([])
        for _ in range(9):
            grid[-1].append('0')
    return 

def ask_and_allocate(grid:list) -> list:
# ask for the value of each slot and allowcate the value to the sudoku 
    output = grid[:]
    for row_index, row in enumerate(grid):
        for index, element in enumerate(row):
            num = '-1'
            while int(num) < 0 or int(num) > 9:
                num = input('Input your row '+ str(row_index+1) +' slot ' + str(index+1) + ' value:' )
                while not num.isdigit():
                    num = input('Input your row '+ str(row_index+1) +' slot ' + str(index+1) + ' value:' )
            output[row_index][index] = num
        break
    return output

def analyse_row(row: list) -> list:
# to analyse a row/column of elements to suggest possible values () 
    # [3,0,0,4,0,8,5,1,0] check 3rd pos (index == 2)
    number_list = [1,2,3,4,5,6,7,8,9]
    # print('row is',row)
    for number in row:
        # print('numebr is',number)
        if number in number_list:
            # print('YES')
            number_list.remove(number)
    return number_list

def merge_possible_values(number_list: list, number_list1: list) -> list:
# to merge the results of analyse_row function for the row and column of a certain value. 
    return [x for x in number_list if x in number_list1]

def transpose_sudoku(sudoku: list) -> list:
# to exchange the row and coolumn value of the grid
    output =[]
    allotcate_placeholder_data(output)
    for row in range(9):
        for column in range(9):
            output[column][row] = sudoku[row][column]
    return output
    
def update_possible_values(grid_possible_values: list, row_index: int, column_index: int):
# calls a function to update possible_values list (possible_values: list, coordinates: list) -> (possible_values: list)
    transposed_sudoku = transpose_sudoku(sudoku)
    if sudoku[row_index][column_index] == 0:
        grid_possible_values[row_index][column_index] = merge_possible_values(analyse_row(sudoku[row_index]),analyse_row(transposed_sudoku[column_index]))
    else:
        grid_possible_values[row_index][column_index] = 0
    return grid_possible_values

def fill_in_answer_and_update_grid_possible_values(possible_values: int, row_index: int, column_index: int, grid_possible_values: list):
#fill in the answer on the sudoku 
    sudoku[row_index][column_index] = possible_values
    # update whole row and column for the grid_possible_values
    
    # update_possible_values(grid_possible_values, row_index, column_index)
    for i in range(9):
        # top to bottom
        grid_possible_values = update_possible_values(grid_possible_values, i, column_index)
        # left to right
        grid_possible_values = update_possible_values(grid_possible_values, row_index, i)
        
    print('\nreplaced location is '+str(row_index)+','+str(column_index)+' with the value of ',possible_values)
    for i in range(9):
        print(grid_possible_values[i])
    return 
def check_completeness(sudoku: list) -> bool:
    # print_grid(sudoku)
    for row in sudoku:
        if 0 in row:
            # print('False')
            return False
    # print('True')
    return True 

def solve(sudoku: list) -> list:
# solves all the values in sudoku and returns the result out
    transposed_sudoku = transpose_sudoku(sudoku)
    grid_possible_values = []
    # calls a function on all locations to analyse the possible values the specific slot can be (coordinates: list, sudoku: list) -> (possible_values: list)
    for row_index, row in enumerate(sudoku):
        grid_possible_values.append([])
        for column_index, number in enumerate(row):
            grid_possible_values[-1].append([])
            # print(column_index)
            grid_possible_values = update_possible_values(grid_possible_values, row_index, column_index)
    # Testing the functions for analyse_row,merge_possible_values and variable grid_possible_values
    
    # print(analyse_row(sudoku[8]),analyse_row(transposed_sudoku[8]))
    # print(merge_possible_values(analyse_row(sudoku[8]),analyse_row(transposed_sudoku[8])))
    # print('\n Printing grid_possible_values:')
    # for i in range(9):
    #     print(grid_possible_values[i])
        
    # calls a function to scan all the possible_values list for a suitable value for one slot and returns the corrected sudoku  (possible_values: list, sudoku: list) -> ( coordinates: list, sudoku: list)
    # calls a function to check for any 0s in the sudoku (sudoku: list) -> (complete: bool)
    # while True:
    for _ in range(10):
        for row_index, row in enumerate(grid_possible_values):
            for column_index, possible_values in enumerate(row):
                if type(possible_values) == list:
                    if len(possible_values) == 1:
                        fill_in_answer_and_update_grid_possible_values(possible_values[0], row_index, column_index, grid_possible_values)
        if check_completeness(sudoku) == True:
            break
    for i in range(9):
        print(grid_possible_values[i])
    return 

def check_validity_on_row(sudoku: list) -> bool:
# checks the validity of sudoku in a row by checking whether there is repeated value
    for row in sudoku:
        mem = []
        for number in row:
            if number in mem:
                return False
            elif number == 0:
                pass
            else: 
                mem.append(number)
    return True

def check_validity(sudoku: list) -> bool:
# check whether the sudoku makes sense or not i.e are there any duplicated numbers:
    if check_validity_on_row(sudoku) and check_validity_on_row(transpose_sudoku(sudoku)):
        print('\nSECURED! Sudoku is valid!')
        return
    else:
        print('ERROR, GRID IS NOT CORRECT')
        exit()

def check_data_validity(data: list):
# checks the vailidity of the data inputted 
    if len(data) != 9:
        print('ERROR, GRID IS NOT CORRECT ON ROW NUMBERS')
        exit()
    for row_index, row in enumerate(data):
        if len(row) != 9:
            print('ERROR, GRID IS NOT CORRECT ON ROW ' + row_index)
            exit()

def allocate_debugging_data(sudoku: list):
    data = '500467309 903810427 174203000 231976854 857124090 496308172 000089260 782641005 010000708'
    data_very_hard = '000801000 000000043 500000000 000070800 000000100 020030000 600000075 003400000 000200600'
    # link at: https://images.app.goo.gl/DmzxJFVMcmPXDYjM7
    chosen_data = data1
    formatted_data = chosen_data.split()
    check_data_validity(formatted_data)
    for row in range(9):
        for column in range(9):
            sudoku[row][column] = int(formatted_data[row][column])
    return

sudoku = []
allotcate_placeholder_data(sudoku)
allocate_debugging_data(sudoku)
# ask_and_allocate(sudoku)
check_validity(sudoku)
print_grid(sudoku)
solve(sudoku)
check_validity(sudoku)
print_grid(sudoku)
