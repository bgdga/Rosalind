#File path for my system:  /home/ccmb/Downloads/easy.csv    hard.csv    harder.csv
#Average time taking to solve                 easy code:    4 seconds
#                                             hard code:    not-stipulated (more than 10 minutes)
#                                             harder code:  not-stipulated (more than 10 minutes)

#Using my logic of row, column, sub-box dictionary based sudoku solver.: Taken help of chatGPT in coding.



import pandas as pd
import numpy as np
import time

# Function to convert string to 9x9 matrix
def str_to_matrix(s):
    # Convert string to list of digits
    digit_list = [int(d) for d in s]
    # Convert list to 9x9 numpy matrix
    return np.array(digit_list).reshape(9, 9)

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


# Check the results
#print(df.head())

def create_index_dicts():
    row_indices = {i: i // 9 for i in range(81)}
    column_indices = {i: i % 9 for i in range(81)}
    sub_box_indices = {i: (i // 27 * 3 + (i % 9) // 3) for i in range(81)}
    return row_indices, column_indices, sub_box_indices

def solve_sudoku(puzzle, row_indices, column_indices, sub_box_indices):
    def is_valid(puzzle, row, col, num):
        # Check if the number already exists in the row
        if num in puzzle[row]:
            return False

        # Check if the number already exists in the column
        for i in range(9):
            if num == puzzle[i][col]:
                return False

        # Check if the number already exists in the sub-box
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if num == puzzle[i][j]:
                    return False

        return True

    def solve(puzzle):
        for i in range(81):
            row = row_indices[i]
            col = column_indices[i]
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve(puzzle):
                            return True
                        puzzle[row][col] = 0  # Backtrack
                return False
        return True

    # Create a copy of the puzzle to avoid modifying the original
    solved_puzzle = [row[:] for row in puzzle]

    # Solve the puzzle
    if solve(solved_puzzle):
        return solved_puzzle
    else:
        return None

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

    # Create the index dictionaries
    row_indices, column_indices, sub_box_indices = create_index_dicts()

    # Solve the Sudoku puzzle
    solved_puzzle = solve_sudoku(puzzle, row_indices, column_indices, sub_box_indices)

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
print(f"Accuracy: {accuracy:.2f}%")
print(f"Total Iterations: {total_iterations}")
print(f"Time Used: {elapsed_time:.2f} seconds")
