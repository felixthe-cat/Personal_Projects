import copy 

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

def analyse_3x3_box(row_index: int, column_index:int) -> list:
    number_list = [1,2,3,4,5,6,7,8,9]
    box_row = row_index // 3
    box_column = column_index // 3
    for row_index1 in range(box_row*3,box_row*3+3):
        for column_index1 in range(box_column*3,box_column*3+3):
            # print(sudoku[row_index1][column_index1])
            if sudoku[row_index1][column_index1] in number_list:
                number_list.remove(sudoku[row_index1][column_index1])
# debugging tool 
    # if row_index ==0 and column_index ==0:
    #     print('\nThe Box analyssis is: for row '+str(row_index)+' '+str(column_index))
    #     print('The box_row and box_column is '+str(box_row)+' '+ str(box_column))
    #     print(number_list)
    return number_list
    

def merge_possible_values(number_list: list, number_list1: list, number_list2: list) -> list:
# to merge the results of analyse_row function for the row and column of a certain value.
    tmp_list = [x for x in number_list if x in number_list1]
    output = []
    for number in tmp_list:
        for number1 in number_list2:
            if number == number1:
                output.append(number)
    # print('The numebr lists are: ')
    # print(number_list, number_list1, number_list2)
    # print('the output is: ')
    # print(tmp_list)
    # print(output)
    return output 

def transpose_sudoku(sudoku: list) -> list:
# to exchange the row and coolumn value of the grid
    output =[]
    allotcate_placeholder_data(output)
    for row in range(9):
        for column in range(9):
            output[column][row] = sudoku[row][column]
    return output
    
def update_possible_values(dummy_grid_possible_values: list, row_index: int, column_index: int, sudoku: list):
# calls a function to update possible_values list (possible_values: list, coordinates: list) -> (possible_values: list)
    transposed_sudoku = transpose_sudoku(sudoku)
    if sudoku[row_index][column_index] == 0:
        dummy_grid_possible_values[row_index][column_index] = merge_possible_values(analyse_row(sudoku[row_index]),analyse_row(transposed_sudoku[column_index]),analyse_3x3_box(row_index, column_index))
    else:
        dummy_grid_possible_values[row_index][column_index] = 0
    return dummy_grid_possible_values

def fill_in_answer_and_update_grid_possible_values(possible_values: int, row_index: int, column_index: int, dummy_grid_possible_values: list, sudoku: list):
#fill in the answer on the sudoku 
    sudoku[row_index][column_index] = possible_values
    # update whole row and column for the dummy_grid_possible_values
    
    # update_possible_values(dummy_grid_possible_values, row_index, column_index)
    for i in range(9):
        # top to bottom
        dummy_grid_possible_values = update_possible_values(dummy_grid_possible_values, i, column_index, sudoku)
        # left to right
        dummy_grid_possible_values = update_possible_values(dummy_grid_possible_values, row_index, i, sudoku)
        
    print('\nreplaced location is '+str(row_index)+','+str(column_index)+' with the value of ',possible_values)
    for i in range(9):
        print(dummy_grid_possible_values[i])
    return 

def row_col_box_possible_list_generator(grid_possible_values: list,row_index: int, column_index: int)-> int:
# returns the three lists of possible_values in the same row, column and box from the specific coordinate, NOT including itself
    row_possible_list = grid_possible_values[row_index][:column_index] + grid_possible_values[row_index][column_index+1:]
    col_possible_list = transpose_sudoku(grid_possible_values)[column_index][:row_index] + transpose_sudoku(grid_possible_values)[column_index][row_index+1:]
    box_possible_list = []
    
    box_row = row_index // 3
    box_column = column_index // 3
    for row_index1 in range(box_row*3,box_row*3+3):
        for column_index1 in range(box_column*3,box_column*3+3):
            if row_index1 != row_index or column_index != column_index1:
                box_possible_list.append(grid_possible_values[row_index1][column_index1])
            # debugging tool 
            # else:
                # print(column_index, column_index1, row_index, row_index1)
    return [row_possible_list, col_possible_list, box_possible_list]
    

def check_completeness(sudoku: list) -> bool:
    # print_grid(sudoku)
    for row in sudoku:
        if 0 in row:
            # print('False')
            return False
    # print('True')
    return True 

def generate_grid_possible_values(sudoku: list)-> list:
# calls a function on all locations to analyse the possible values the specific slot can be (coordinates: list, sudoku: list) -> (possible_values: list)
    grid_possible_values =[]
    for row_index, row in enumerate(sudoku):
        grid_possible_values.append([])
        for column_index, number in enumerate(row):
            grid_possible_values[-1].append([])
            # print(column_index)
            grid_possible_values = update_possible_values(grid_possible_values, row_index, column_index, sudoku)
    return grid_possible_values

def contains_duplicate(target_pointer: int, neighbour_possible_value: list) -> bool :
    for tmp_pointer in neighbour_possible_value:
        # print('target_pointer is', target_pointer, 'tmp_pointer is', tmp_pointer)
        if target_pointer == tmp_pointer:
            return True
    return False 
        

def find_uniqueness(target_list: list, related_list: list)-> int: 
    for target_pointer in target_list:
        # print('target_pointer is', target_pointer)
        unique = True 
        for neighbour_possible_value in related_list:
            if type(neighbour_possible_value) == list:
                if contains_duplicate(target_pointer, neighbour_possible_value):
                    # print('neighbour_possible_value is', neighbour_possible_value)
                    # print('target_pointer is', target_pointer, 'and it is duplicated')
                    unique = False
                    break
        if unique == True:
            # print('UNIQUE')
            return target_pointer
    return 0
        
def check_contradiction(dummy_grid_possible_values: list) -> bool:
    for row in dummy_grid_possible_values:
        for pointer in row:
            if pointer != 0:
                if len(pointer) == 0:
                    print('The element found to be invalid is', pointer, 'in', row)
                    return True
    return False
                

def method_one(sudoku: list) -> list:
# solves all the values in sudoku and returns the result out
    print('Start of Method 1')
    transposed_sudoku = transpose_sudoku(sudoku)
    grid_possible_values = generate_grid_possible_values(sudoku)
    
    # Testing the functions for analyse_row,merge_possible_values and variable grid_possible_values
    
        # print(analyse_row(sudoku[8]),analyse_row(transposed_sudoku[8]))
        # print(merge_possible_values(analyse_row(sudoku[8]),analyse_row(transposed_sudoku[8]), analyse_3x3_box(8,8)))
    print('\n Printing grid_possible_values:')
    for i in range(9):
        print(grid_possible_values[i])
        
    # calls a function to scan all the possible_values list for a suitable value for one slot and returns the corrected sudoku  (possible_values: list, sudoku: list) -> ( coordinates: list, sudoku: list)
    # calls a function to check for any 0s in the sudoku (sudoku: list) -> (complete: bool)
    
    while True:
        # Method 1: only analysing possible values
        updated = False
        for row_index, row in enumerate(grid_possible_values):
            for column_index, possible_values in enumerate(row):
                if type(possible_values) == list:
                    if len(possible_values) == 1:
                        fill_in_answer_and_update_grid_possible_values(possible_values[0], row_index, column_index, grid_possible_values, sudoku)
                        updated = True
                        continue
                    related_list = row_col_box_possible_list_generator(grid_possible_values,row_index, column_index)
                    for i in range(3):
                        if find_uniqueness(grid_possible_values[row_index][column_index], related_list[i]) != 0:
                            fill_in_answer_and_update_grid_possible_values(find_uniqueness(grid_possible_values[row_index][column_index], related_list[i]), row_index, column_index, grid_possible_values, sudoku)
                            updated = True
                            break 
                    if check_contradiction(grid_possible_values):
                        print('Checked to be invalid by check_contradiction function')
                        return [False,]
        if updated == False:
            break
    # to prxint out the grid of possible values
    print('\nGrid of possible values at the end is:')
    for i in range(9):
        print(grid_possible_values[i], end='\n\n')
    print('End of Method 1')
    return [True,sudoku]

def recursive_solving(grid_possible_values: list, trial_history: list, board_history: tuple, grid_possible_values_history: tuple, trial_value_history: dict, times_called: int):
    
    times_called += 1
    print('------------------------------------------------------------------------', times_called)
    
    row_index = 0
    column_index = 0
    while True:
        possible_values = grid_possible_values[row_index][column_index]
        if type(possible_values) == list:
            print('\nGrid of possible values at initiation is:')
            for i in range(9):
                print(grid_possible_values[i], end='\n\n')
            print('possible_values are', possible_values)
            trial_value = possible_values[0]
            trial_history.append((row_index, column_index))
            if len(grid_possible_values[row_index][column_index]) != 1:
                grid_possible_values[row_index][column_index].pop(0)
            else: 
                grid_possible_values[row_index][column_index] = 0
            trial_value_history[trial_history[-1]] = trial_value
            
            # print('trial_value is', trial_value)
            # print('trial_history is', trial_history)
            # print('trial_value_history', trial_value_history)
            # print('\nGrid of possible values after popping is:')
            for i in range(9):
                print(grid_possible_values[i], end='\n\n')
            # Reset grid_possible_values and sudoku
            tmp_grid_possible_values = copy.deepcopy(grid_possible_values)
            tmp_sudoku = copy.deepcopy(board_history[-1])
            # print('\n\nSudoku before Error')
            # print(sudoku)
            print_grid(sudoku)
            fill_in_answer_and_update_grid_possible_values(trial_value, row_index, column_index, tmp_grid_possible_values, tmp_sudoku)
            grid_possible_values = list(grid_possible_values_history)
            sudoku_validity = method_one(tmp_sudoku)
            print('sudoku_validity[0] is', sudoku_validity[0])
            if not sudoku_validity[0]:
                print('Sudoku not valid by back Propagation')
                # print('Trial value is')
                # print('trial_value is', trial_value)
                # print('trial_history is', trial_history)
                # print('trial_value_history', trial_value_history)
                # print('\nGrid of possible values after one Propagation is:')
                # for i in range(9):
                #     print(grid_possible_values[i], end='\n\n')
                
                return recursive_solving(grid_possible_values, trial_history, board_history, grid_possible_values_history, trial_value_history, times_called)
            else:
                print('End of Recursive_solving')
                return sudoku_validity[1]
        else:
            if column_index != 8:
                column_index += 1
            else: 
                column_index = 0
                row_index += 1
    print('Stuck in While Loop')

def method_two(sudoku: list) -> list:
# Method 2: Back Propagation
# when method 1 no longer works:
    # initial setup 
    transposed_sudoku = transpose_sudoku(sudoku)
    grid_possible_values = generate_grid_possible_values(sudoku)
    
    trial_history = []
    board_history = tuple([sudoku])
    grid_possible_values_history = tuple(grid_possible_values)
    trial_value_history = {}
    
    # debugging tool 
    print('board_history before error')
    print(board_history)
    
    # recursive
    times_called = 0
    answer = recursive_solving(grid_possible_values, trial_history, board_history, grid_possible_values_history, trial_value_history, times_called)
    # while True: 
    #     results = recursive_solving(grid_possible_values)
    #     if not results[0]:
    #         grid_possible_values = results[1]
    #         recursive_solving(grid_possible_values)
    #         exit()
    print('End of Method 2')
    return answer

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
    data_for_box_analysis = '012000000 345000000 678000000 000000000 000000000 000000000 000000000 000000000 000000000'
    # link at: https://images.app.goo.gl/DmzxJFVMcmPXDYjM7
    data_medium = '000500006 000870302 270300081 000034900 793050614 008790000 920003057 506087000 300005000'
    # https://www.canstockphoto.com/sudoku-game-with-answers-simple-vector-82405983.html 000500006 000870302 270300081 000034900 793050614 008790000 920003057 506087000 300005000
    chosen_data = data_very_hard
    formatted_data = chosen_data.split()
    check_data_validity(formatted_data)
    for row in range(9):
        for column in range(9):
            sudoku[row][column] = int(formatted_data[row][column])
    return

sudoku = []
allotcate_placeholder_data(sudoku)
allocate_debugging_data(sudoku)

# debug process
    # grid_possible_values = generate_grid_possible_values(sudoku)
    # row_index = 2
    # column_index = 6
    # related_list = row_col_box_possible_list_generator(grid_possible_values,row_index,column_index)
    # for i in related_list:
    #     print (i)
    # if find_uniqueness(grid_possible_values[row_index][column_index], related_list[1]) != 0:
        
    #     fill_in_answer_and_update_grid_possible_values(find_uniqueness(grid_possible_values[row_index][column_index], related_list[1]), row_index, column_index, grid_possible_values)
    
    # exit()


# ask_and_allocate(sudoku)
check_validity(sudoku)
print_grid(sudoku)
method_one(sudoku)
if check_completeness(sudoku) == False:
    print('Back Propagation Starts: ')
    sudoku = method_two(sudoku)
    # sudoku = copy.deepcopy(method_two(sudoku))
    print('End of the whole thing')
check_validity(sudoku)
print_grid(sudoku)
