#Sudoku teJET version :code version 5.

import multiprocessing
import pandas as pd
import numpy as np
import time
from multiprocessing import Pool

def solve_sudoku(puzzle):
    digits = '123456789'
    rows = 'ABCDEFGHI'
    cols = digits

    def cross(a, b):
        return [s + t for s in a for t in b]

    positions = cross(rows, cols)
    unittuple = (
        [cross(rows, c) for c in cols] +
        [cross(r, cols) for r in rows] +
        [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
    )
    units = dict((s, [u for u in unittuple if s in u]) for s in positions)
    peers = dict((s, set(sum(units[s], [])) - {s}) for s in positions)

    def parse_string(string):
        values = dict((s, digits) for s in positions)
        for s, d in string_values(string).items():
            if d in digits and not assign(values, s, d):
                return False
        return values
                                                                #
    def string_values(string):
        chars = np.array(list(string)).astype(str)
        assert len(chars) == 81
        return dict(zip(positions, chars))
                                                                    #
    def assign(values, s, d):
        other_values = values[s].replace(d, '')
        if all(eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False
                                                                    #
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

    def search(values):
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in positions):
            return ''.join(values[s] for s in positions)  # Combine values into a single string
        n, s = min((len(values[s]), s) for s in positions if len(values[s]) > 1)
        return some(search(assign(values.copy(), s, d)) for d in values[s])

    def some(seq):
        for e in seq:
            if e:
                return e
        return False

    # Solve the puzzle
    values = parse_string(puzzle)
    if values:
        return search(values)
    else:
        return None


# Define a worker function for parallel processing
def solve_sudoku_worker(puzzle):
    return solve_sudoku(puzzle)

# Ask user for CSV file path
csv_path = input("Please enter the path to the CSV file: ")

# Read CSV file
df = pd.read_csv(csv_path)

# Get the column names dynamically
puzzles_col = df.columns[0]
solutions_col = df.columns[1]

# Initialize counters
total_puzzles = len(df)
total_iterations = 0
correctly_solved_puzzles = 0

# Initialize time tracking
start_time = time.time()

# Create a multiprocessing Pool with the number of desired CPU cores
num_cores = multiprocessing.cpu_count()
pool = Pool(processes=num_cores)

# Iterate over the DataFrame rows and solve puzzles in parallel
results = pool.map(solve_sudoku_worker, df[puzzles_col])

# Close the pool to free resources
pool.close()
pool.join()

# Iterate over the results and update counters
for index, row in df.iterrows():
    solved_puzzle = results[index]

    total_iterations += 1
    if solved_puzzle is not None and np.array_equal(solved_puzzle, row[solutions_col]):
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
print(solved_puzzle, row[solutions_col])  # Test sample (last row)

#/home/ccmb/Downloads/harder.csv
