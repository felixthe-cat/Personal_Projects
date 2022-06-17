# from tabulate import tabulate
def print_separating_row():
    print('+ — ' * 9, end='+ \n')
    return 

def print_grid(x:list):
    print('')
    print('           ~ Sudoku Grid ~          ')
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
        break
    return output

def analyse_row(row: list) -> list:
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
    return [x for x in number_list if x in number_list1]

def transpose_sudoku(sudoku: list) -> list:
    output =[]
    allotcate_placeholder_data(output)
    for row in range(9):
        for column in range(9):
            output[column][row] = sudoku[row][column]
    return output

def solve(sudoku: list) -> list:
    # solves all the values in soudku and returns the result out
    transposed_sudoku = transpose_sudoku(sudoku)
    print(analyse_row(sudoku[0]),analyse_row(transposed_sudoku[1]))
    print(merge_possible_values(analyse_row(sudoku[0]),analyse_row(transposed_sudoku[1])))
    
    
    # print_grid(transposed_sudoku)
    # calls a function on placeholder locations to analyse all the possible values the specific slot can be (coordinates: list, sudoku: list) -> (possible_values: list)
    
        # Possible_values = merge_possible_values(analyse_row(row), analyse_row(column))
        # function to analyse a row/column of elements to suggest possible values () 
    # calls a function to scan all the possible_values list for a suitable value for one slot and returns the corrected sudoku  (possible_values: list, sudoku: list) -> ( coordinates: list, sudoku: list)
    # calls a function to update possible_values list (possible_values: list, coordinates: list) -> (possible_values: list)
    # calls a function to check for any 0s in the sudoku (sudoku: list) -> (complete: bool)
    return 

def check_validity_on_row(sudoku: list) -> bool:
    for row_index, row in enumerate(sudoku):
        mem = []
        for index, number in enumerate(row):
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
        return
    else:
        print('ERROR, GRID IS NOT CORRECT')
        exit()

def allocate_debugging_data(sudoku: list):
    data = '500467309 903810427 174203000 231976854 857124090 496308172 000089260 782641005 010000708'.split()
    for row in range(9):
        for column in range(9):
            sudoku[row][column] = int(data[row][column])
    return

sudoku = []
allotcate_placeholder_data(sudoku)
allocate_debugging_data(sudoku)
# ask_and_allocate(sudoku)
check_validity(sudoku)
solve(sudoku)

print_grid(sudoku)
