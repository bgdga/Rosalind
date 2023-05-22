#File path for my system:  /home/ccmb/Downloads/easy.csv    hard.csv    harder.csv
#Average time taking to solve                 easy sudoku:    2.6 seconds
#                                             hard sudoku:    7.0 seconds
#                                             harder sudoku:  18.5 seconds

#Sudoku FASTER version:  code version 2. Modification in v1=Changed the solving method, but continued with my dictionaries concept in it. (Problemn in v2- contains unneccesary steps to convert from string-list-matrix, and back).
#based on : backtracking algorithm + constraint propagation : ChatGPT mediated modified version of my original code.
#Kindly respect the annotations: 5+6+4+3 hours of work. (annotations reflect partially my understanding of this code).
# Code creation= 3+2 hours of work, but with help of chatGPT... (if I had to do it alone, guess how much time it would take ? Ummmmmmmmmmmmmmm............ with current level of my coding language-onl mine, not chatGPT added info- it would take---- an eternity !)   ;)






import pandas as pd                                                                           #to read, and modify input CSV file.
import numpy as np                                                                            #to convert list into matrix (used later).
import time                                                                                   #to count time spent in solving sudoku problem.

                                                                                      # Function to convert string to 9x9 matrix
def str_to_matrix(s):                                                                         #s=input sudoku as string (each one single line of sudoku in CSV file)
                                                                                      # Convert string (s) to list of digits (digit_list)
    digit_list = [int(d) for d in s]                                                          #d=a variable, can be any letter, variable for digits in string s.
                                                                                      # Convert list to 9x9 numpy matrix
    return np.array(digit_list).reshape(9, 9)                                                 #now, 'digit_list' variable is a 9*9 numpy MATRIX. List replaced by matrix.

                                                                                      #defining method to solve given sudoku (converted into matrix). incluids many sub-defined methods.
def solve_sudoku(puzzle):
                                                                                      #assigning variables to locate matrix positions.
    digits = '123456789'
    rows = 'ABCDEFGHI'
    cols = digits

                                                                                      #sub-Method/function to create position-list, dictionary (row, column, boxes positions)- of matrix.
    def cross(a, b):                                                                          #a=row (s=A,B,C...I), b=column(t=1,2,3...9) (s,t can be any letter, variables)
        return [s + t for s in a for t in b]                                                  #Cross function is to RETURNS LIST of matrix positions : [ A1, A2,.... B1,B2,.... I1,...I9 ]

                                                                                      #calling cross function
    positions = cross(rows, cols)                                                     #to generate LIST of ALL matrix positions (list named here as: positions) (here, rows~a, columns~b of cross function)
    unittup = (                                                                       #to generate TUPLE() of LISTs[]. LIST of row positions, column positions, BOXES (3*3) positions. : ([[row1-A1,B1..][row2- A2,..I2]...[row9]], [[column A- A1, A2..][col B- B1,...B9]...[col I]], [[box 1] [box 2]...[box 9]])
        [cross(rows, c) for c in cols] +                                                      #to generate LIST of ROWS. [[row1-A1,B1..][row2- A2,..I2]...[row9]]. c can be any letter, a variable.
        [cross(r, cols) for r in rows] +                                                      #to generate LIST of COLUMNS. [[column A- A1, A2..][col B- B1,...B9]...[col I]]. r can be any letter, a variable.
        [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]       #to generate a LIST of all the BOXES in the Sudoku puzzle. 'rs'= rows that make a box ('ABC', 'DEF', 'GHI'). 'cs'= columns that make a box ('123', '456', '789'). rs,cs-variables- can be any letter. Cross fn gives 9 lists of positions in sudoku for 9 boxes. [[box 1- A1, A2, A3, B1,B2...C3] [box 2]...[box 9]].
    )
    units = dict((s, [u for u in unittup if s in u]) for s in positions)               #(units-vvi) Using 'positions' LIST & 'unittup' TUPLE (made above), to make DICTIONARY named-'units'. Dict content-- s= all positions in sudoku (from positions)- linked to - u= row, col, box positions (from unittup).
    peers = dict((s, set(sum(units[s], [])) - {s}) for s in positions)                 #(peers-vvi) Using 'units' DICT & 'positions' LIST (made above), to make DICTIONARY named-peers. Dict content-- peers of each position in a Sudoku puzzle. Peers~ In Sudoku, the peers of a  (position) are other positions that are in the same row, column, or 3x3 box.
                                                                                              #EXPLINING ABOVE COMMAND: units[s] retrieves the list of units (groups of positions) that the position s belongs to. sum(units[s], []) flattens the list of units into a single list of positions. set(sum(units[s], [])) converts the flattened list of positions into a set, removing any duplicate positions.
                                                                                              # {s} creates a set containing only the position s. set(sum(units[s], [])) - {s} subtracts the set containing s from the set of peers, removing s itself from the set of peers. The resulting set of peers is assigned as the value corresponding to the position s in the dictionary.

                                                                                     #To Convert the input STRING (puzzle string) into a dictionary. Dict CONTENT-POSITION NAME (A1,G2,...) : Corresponding digit OF input puzzle string.
    def string_values(string):                                                                 #This function takes a string (puzzle string) as input.
        chars = np.array(list(string)).astype(str)                                             #converts INPUT STRING into a 'char'-named array.
        assert len(chars) == 81                                                                #It checks whether the length of the chars array is equal to 81.     #assert~In Python, assertions are used to verify that certain conditions are true during the execution of the program. If the condition specified in the assertion statement is false, it raises an AssertionError exception, indicating that there is an issue with the program logic.
        return dict(zip(positions, chars))                                                     #returns 'string' Dict. content-positions (from 'positions' list): digits (from 'chars' array, i.e. puzzle digits).

                                                                                     #To Parse the Sudoku string and 'check if values in string are digits', then create the 'values' dictionary = positions: digits (puzzles).    #Parsing refers to the process of analyzing and interpreting a given input
    def parse_string(string):                                                                 #parse_string(string): This function takes a string as input, Sudoku puzzle.
        values = dict((s, digits) for s in positions)                                         #It creates a dictionary named- 'values'. Dict content-positions (from positions list) : digits '123456789' (variable assigned above).
        for s, d in string_values(string).items():                                            #It iterates over the items of the 'string' dictionary (made above in string_value fn). #calling string_value function.
            if d in digits and not assign(values, s, d):                     ###              #For each position-digit pair in 'string' dict, it checks if the 'value' is a 'digit', and calls the 'assign' function (defined below).
                return False                                                                  #If the assign function returns False, indicating a contradiction, it returns False.      #return false~  current execution path is not valid or does not satisfy the required conditions. Drop the job here, move to next line command.
        return values                                                                         #Otherwise, it returns the 'updated 'values' dictionary' (earlier 1-9 digits of 'values' dict, replaced by puzzle-digit from 'string' dict). So, now 'values' is the dictionary having our puzzle-digits.
                                                                            ###--- this and related steps (assign, string value) can be modified/removed if we consider that input file has no error. if no error, no need to check.

                                                                                     #Assigns a specific digit d to a position s in the values dictionary and eliminates d as a possibility from other related positions.
    def assign(values, s, d):                                                                #This function assigns a value d to the position s in the values dictionary and propagates the constraints to other positions. #"Propagating the constraints" means applying these rules and limitations to narrow down the possible values for each square based on the values of its peers.
        other_values = values[s].replace(d, '')                                              #It creates a new 'other_values' string by replacing d with an empty string in the current value of position s.
        if all(eliminate(values, s, d2) for d2 in other_values):                             #It checks if the elimination of d from all other positions in the same units as s is successful, by calling the 'eliminate function' (defined below) for each value in 'other_values'.
            return values                                                                    #If the elimination is successful for all values, it returns the updated 'values' dictionary.
        else:                                                                                #Otherwise, it returns False indicating a contradiction.
            return False

                                                                                     #Eliminates the possibility of digit d from a position s in the values dictionary and performs additional elimination logic based on 'constraints' and 'peers' of s.
    def eliminate(values, s, d):                                                            #
        if d not in values[s]:                                                              #If d is not present in values[s],
            return values                                                                   #it returns the values dictionary as there is no need for elimination.
        values[s] = values[s].replace(d, '')                                                #Otherwise, it removes d from values[s].
        if len(values[s]) == 0:                                                             #If the length of values[s] becomes zero, indicating a contradiction,
            return False                                                                    #it returns False.
        elif len(values[s]) == 1:                                                           #If the length of values[s] becomes one,
            d2 = values[s]                                                                  #it assigns the remaining value d2 to s and
            if not all(eliminate(values, s2, d2) for s2 in peers[s]):                       #recursively calls eliminate on all peers of s.
                return False
        for u in units[s]:                                                                  #It also checks the constraints for each unit that s belongs to,
            dplaces = [s for s in u if d in values[s]]                                      #ensuring that each value d has a place in at least one position within the unit.
            if len(dplaces) == 0:                                                           #If any unit has no place for d,
                return False                                                                #it returns False.
            elif len(dplaces) == 1:
                if not assign(values, dplaces[0], d):
                    return False
        return values                                                                       #it returns the updated 'values' dictionary.

                                                                     ###            ###(AI done mistake- didn't call this function anywhere for printing it's outcomes. No use in solving sudoku.) Displays the Sudoku string with the current state of values for each position.
    def display(values):                                                                    #This function takes the 'values' dictionary and displays the Sudoku puzzle in a visually formatted way.
            width = 1 + max(len(values[s]) for s in positions)                              #It determines the appropriate width for each position based on the maximum length of the values,
            line = '+'.join(['-' * (width * 3)] * 3)                                        #creates a separator line. #It adds horizontal separators '-' for every third row.
            for r in rows:                                                                  #and then iterates over the rows and columns to print the values.
                print(''.join(values[r + c].center(width) + ('|' if c in '36' else '') for c in cols))   #It adds vertical separators '|' for every third column.
                if r in 'CF':
                    print(line)
            print()

                                                                                     #Searches for a 'solution to the Sudoku' puzzle using a 'backtracking algorithm', exploring possible assignments of digits to positions.
    def search(values):                                                                     #This function is a 'depth-first search algorithm' that attempts to solve the Sudoku puzzle recursively using 'constraint propagation'.
        if values is False:                                                                 # It checks if values is False, indicating a contradiction, and
            return False                                                                    # returns False in that case.
        if all(len(values[s]) == 1 for s in positions):                                     #If all positions have only one possible value,
            return values                                                                   #it returns values as the solution.
        n, s = min((len(values[s]), s) for s in positions if len(values[s]) > 1)            #Otherwise, it selects the position s with the fewest possibilities and
        return some(search(assign(values.copy(), s, d)) for d in values[s])                 #recursively calls 'search' on each possible value d for s using the 'assign' function. It returns (calling 'some') the first successful result obtained from the recursive calls or False if none of them succeed.

                                                                                    #Iterates over a sequence and returns the first non-false element encountered.
    def some(seq):                                                                          #This function takes a sequence 'seq' and,
        for e in seq:                                                                       #returns the first element that is considered true (not False, None, or an empty string).
            if e:
                return e
        return False                                                                        #If no true element is found, it returns False.

                                                                                    #Solve the puzzle:  The main part of the code that solves the Sudoku puzzle by first parsing the string, then searching for a solution using the search function, and returning the solved puzzle as values. If the puzzle cannot be solved, it returns None.
    values = parse_string(puzzle)                                                           # It first parses the puzzle string using parse_string function and assigns the result to variable named-values.
    if values:                                                                              #If values is not False, indicating a valid puzzle,
        return search(values)                                                               #it calls the search function on values, to find the solution. If a solution is found, it returns the solution (values)
    else:                                                                                   #Otherwise,
        return None                                                                         #it returns None.




#Now, use of the methods created above, to solve our problem.__________________________________________________________________________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________




                                                                                     # Ask user for CSV file path  #CSV, which contains sudoku questions and solutions under 2 different columns with headers)
csv_path = input("Please enter the path to the CSV file: ")

                                                                                     # Read CSV file (uses panda module, imported above as pd, at start of this code)
df = pd.read_csv(csv_path)                                                                    #stores input file as named 'df'

                                                                                     # Get the column names dynamically                                                            #sudoku: questions and solutions - 2 different columns, with different header name in different files, so dynamic header function used.
puzzles_col = df.columns[0]                                                                   #any header in original file is replaced by 'puzzles_col', in 0th index (i.e. 1st) column of file 'df'.
solutions_col = df.columns[1]                                                                 #any header in original file is replaced by 'solutions_col', in 1st index (i.e. 2nd) column of file 'df'.

                                                                                     # Apply the function to the puzzles and solutions columns   #calling
df[puzzles_col] = df[puzzles_col].apply(str_to_matrix)                                        #converts the puzzles_col of df file, into matrix. each one strings are replaced by corresponding matrix. i.e., now, df file has matrices in 1st column under header 'puzzles_col'. Uses str_to_matrix method, defined earlier.
df[solutions_col] = df[solutions_col].apply(str_to_matrix)                                    #converts the solutions_col of df file, into matrix. each one strings are replaced by corresponding matrix. i.e., now, df file has matrices in 2nd column under header 'solutions_col'. Uses str_to_matrix method, defined earlier.

                                                                                     # Initialize counters
total_puzzles = len(df)                                                                       #len(df)= length of df file. i.e. number of matrices, i.e. number of sudoku questions given as string in csv file.
total_iterations = 0                                                                                                                                          #assigning a variable, starting with zero, for counting iterations.
correctly_solved_puzzles = 0                                                                  #assigning a variable, starting with zero, for counting correctly_solved_puzzles.

                                                                                     # Initialize time tracking (to get time taken to solve all given sudoku problems).
start_time = time.time()                                                                      #using imported 'time module', imported at start of this code. STARTS the time counter just BEFORE following commands starts solving the given problem.

                                                                                     # Iterate over the DataFrame (df file) rows
for index, row in df.iterrows():                                                              #FOR LOOP, which iterates over df file's each row (df-iter-rows). one row= 2 columns (question and solutions). So, in one iteration-the code under this for loop will solve one sudoku problem (accessing data of 1st column) of one row; AND will use solution (2nd column data) of same row to check the accuracy of code-provided answer. Then, the FOR LOOP will move top next index no. of rows.
                                                                                     # Get the puzzle and solution dynamically
    puzzle = row[puzzles_col]                                                                 # one-by-one (for loop) fetches the puzzles (matrix format) stored in puzzles_col of df file.
    solution = row[solutions_col]                                                             # one-by-one (for loop) fetches the solutions (matrix format) stored in solutions_col of df file.

                                                                                     # Solve the Sudoku puzzle
    puzzle_str = ''.join(str(d) for d in puzzle.flat)                                         #Work needed here-see below line. This command: converts matrix into flat list array. then joins elements of lists to make string. uses this string to feed into solve_sudoku method to get solutions.
    '''puzzle conversion into matrix not needed. (above step and related steps), bcz code is changing the matrix back into string before solving. see where change can be done (steps involving string- to matrix conversion-then matrix to string conversion: remove if not affects the positions and dictionaries), to remove these extra steps and make code more efficient.'''

    solved_puzzle = solve_sudoku(puzzle_str)                                                  #calling method created above to solve sudoku... under for loop, solves puzzles-one by one. Stores solution in a new variable- 'solved_puzzle'

                                                                                    # Convert the solved puzzle back to a matrix
    if solved_puzzle is not None:                                                             # MEANS, if code finds at least one answer (code-given solution of sudoku) for the given sudoku question in that row,
        solved_puzzle = np.array(list(solved_puzzle.values())).reshape(9, 9).astype(int)      #Then, answer of puzzle stored in 'solved_puzzle' variable in STRING form, (2 steps earlier), will be converted back into - LIST- and then into MATRIX. It will be used to COMPARE WITH solution provided with question in CSV file (df file).
    '''this above step is also not needed. change it while making change into code.'''

                                                                                    # Update counters and check accuracy
    total_iterations += 1                                                                     # FOR LOOP ran once, means solved one sudoku problem. SO, one iteration counted.
    if solved_puzzle is not None and np.array_equal(solved_puzzle, solution):                 #Comparing answer of puzzle provided by code to solution given with question in CSV file. (df file). if both same, means code provided solution is correct.
        correctly_solved_puzzles += 1                                                         #adds one to correctly_solved_puzzles variable, if 'both' of above requisite correct ('and' command in above line). i.e., if there is a solution provided by code and that solution is as same as the solution given with question.

                                                                                    # Calculate elapsed time
elapsed_time = time.time() - start_time                                                       #using imported 'time module', imported at start of this code. STOPS the time counter just AFTER above commands ends with their work.

                                                                                    # Calculate accuracy
accuracy = (correctly_solved_puzzles / total_puzzles) * 100                                   #no need to explain ;)

                                                                                    # Print results
print(f"Total Puzzles: {total_puzzles}")
print(f"Correctly Solved Puzzles: {correctly_solved_puzzles}")
print(f"Accuracy: {accuracy:.3f}%")                                                           #prints accuracy with 3 decimal points. (change number before 'f' to change number of decimal points up to which you want to print the value)
print(f"Total Iterations: {total_iterations}")
print(f"Time Used: {elapsed_time:.8f} seconds")                                               #prints time with 8 decimal points.




'''


The logic behind the Sudoku-solving algorithm used in this above code is based on a backtracking algorithm combined with constraint propagation. Here's a breakdown of the main steps:

1. **Data Representation**: The Sudoku puzzle is represented as a dictionary of possible values for each position on the Sudoku string.
2. **Constraint Propagation**: The algorithm starts by applying constraint propagation to reduce the search space. It eliminates values from the possible values of each position based on the constraints of the Sudoku puzzle (no repeated values in the same row, column, or 3x3 sub-string).
3. **Backtracking Search**: After constraint propagation, the algorithm performs a depth-first search to find a solution. It selects an unfilled position with the fewest possible values and tries each value recursively. If a contradiction is reached (a position has no possible values), it backtracks to the previous position and tries a different value.
4. **Optimization**: The algorithm uses various optimization techniques, such as the "minimum remaining values" and "degree heuristic" to choose the most constrained position and value to try first. This helps in reducing the search space and improving efficiency.

By combining constraint propagation and backtracking search, the algorithm is able to solve Sudoku puzzles efficiently. It systematically explores the possible solution space, considering only valid partial assignments, until a valid solution is found or all possibilities have been exhausted.
Note: The code also includes some additional helper functions for string parsing and visualization, but the core logic lies in the `parse_string`, `assign`, `eliminate`, and `search` functions.
'''




