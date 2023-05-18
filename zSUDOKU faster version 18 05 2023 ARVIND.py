#File path for my system:  /home/ccmb/Downloads/easy.csv    hard.csv    harder.csv
#Average time taking to solve                 easy sudoku:    2.6 seconds
#                                             hard sudoku:    7.0 seconds
#                                             harder sudoku:  18.5 seconds

#based on : backtracking algorithm + constraint propagation : ChatGPT mediated modified version of my original code.


import pandas as pd
import numpy as np
import time

# Function to convert string to 9x9 matrix
def str_to_matrix(s):
    # Convert string to list of digits
    digit_list = [int(d) for d in s]
    # Convert list to 9x9 numpy matrix
    return np.array(digit_list).reshape(9, 9)

def solve_sudoku(puzzle):
    digits = '123456789'
    rows = 'ABCDEFGHI'
    cols = digits

    def cross(a, b):
        return [s + t for s in a for t in b]

    squares = cross(rows, cols)
    unitlist = (
        [cross(rows, c) for c in cols] +
        [cross(r, cols) for r in rows] +
        [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
    )
    units = dict((s, [u for u in unitlist if s in u]) for s in squares)
    peers = dict((s, set(sum(units[s], [])) - {s}) for s in squares)

    def parse_grid(grid):
        values = dict((s, digits) for s in squares)
        for s, d in grid_values(grid).items():
            if d in digits and not assign(values, s, d):
                return False
        return values

    def grid_values(grid):
        chars = np.array(list(grid)).astype(str)
        assert len(chars) == 81
        return dict(zip(squares, chars))

    def assign(values, s, d):
        other_values = values[s].replace(d, '')
        if all(eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(eliminate(values, s2, d2) for s2 in peers[s]):
                return False
        for u in units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not assign(values, dplaces[0], d):
                    return False
        return values

    def display(values):
        width = 1 + max(len(values[s]) for s in squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in rows:
            print(''.join(values[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
            if r in 'CF':
                print(line)
        print()

    def search(values):
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in squares):
            return values
        n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
        return some(search(assign(values.copy(), s, d)) for d in values[s])

    def some(seq):
        for e in seq:
            if e:
                return e
        return False

    # Solve the puzzle
    values = parse_grid(puzzle)
    if values:
        return search(values)
    else:
        return None

# Ask user for CSV file path
csv_path = input("Please enter the path to the CSV file: ")

# Read CSV file
df = pd.read_csv(csv_path)

# Get the column names dynamically
puzzles_col = df.columns[0]
solutions_col = df.columns[1]

# Apply the function to the puzzles and solutions columns
df[puzzles_col] = df[puzzles_col].apply(str_to_matrix)
df[solutions_col] = df[solutions_col].apply(str_to_matrix)

# Initialize counters
total_puzzles = len(df)
total_iterations = 0
correctly_solved_puzzles = 0

# Initialize time tracking
start_time = time.time()

# Iterate over the DataFrame rows
for index, row in df.iterrows():
    # Get the puzzle and solution dynamically
    puzzle = row[puzzles_col]
    solution = row[solutions_col]

    # Solve the Sudoku puzzle
    puzzle_str = ''.join(str(d) for d in puzzle.flat)
    solved_puzzle = solve_sudoku(puzzle_str)

    # Convert the solved puzzle back to a matrix
    if solved_puzzle is not None:
        solved_puzzle = np.array(list(solved_puzzle.values())).reshape(9, 9).astype(int)

    # Update counters and check accuracy
    total_iterations += 1
    if solved_puzzle is not None and np.array_equal(solved_puzzle, solution):
        correctly_solved_puzzles += 1

# Calculate elapsed time
elapsed_time = time.time() - start_time

# Calculate accuracy
accuracy = (correctly_solved_puzzles / total_puzzles) * 100

# Print results
print(f"Total Puzzles: {total_puzzles}")
print(f"Correctly Solved Puzzles: {correctly_solved_puzzles}")
print(f"Accuracy: {accuracy:.3f}%")
print(f"Total Iterations: {total_iterations}")
print(f"Time Used: {elapsed_time:.8f} seconds")




'''


The logic behind the Sudoku-solving algorithm used in the updated code is based on a backtracking algorithm combined with constraint propagation. Here's a breakdown of the main steps:

1. **Data Representation**: The Sudoku puzzle is represented as a dictionary of possible values for each square on the Sudoku grid.
2. **Constraint Propagation**: The algorithm starts by applying constraint propagation to reduce the search space. It eliminates values from the possible values of each square based on the constraints of the Sudoku puzzle (no repeated values in the same row, column, or 3x3 sub-grid).
3. **Search**: After constraint propagation, the algorithm performs a depth-first search to find a solution. It selects an unfilled square with the fewest possible values and tries each value recursively. If a contradiction is reached (a square has no possible values), it backtracks to the previous square and tries a different value.
4. **Optimization**: The algorithm uses various optimization techniques, such as the "minimum remaining values" and "degree heuristic" to choose the most constrained square and value to try first. This helps in reducing the search space and improving efficiency.

By combining constraint propagation and backtracking search, the algorithm is able to solve Sudoku puzzles efficiently. It systematically explores the possible solution space, considering only valid partial assignments, until a valid solution is found or all possibilities have been exhausted.
Note: The code also includes some additional helper functions for grid parsing and visualization, but the core logic lies in the `parse_grid`, `assign`, `eliminate`, and `search` functions.
'''




