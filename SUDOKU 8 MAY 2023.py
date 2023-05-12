#(4) using https://pypi.org/project/py-sudoku/ library. Not workig as given in commands on site.

from sudoku import *






















#(3) modified version of (2).

import time
M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)

    for num in range(1, M + 1, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num

            if Suduko(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False

def convert_to_grid(dataset):
    grid = []
    row_length = int(len(dataset) ** 0.5)  # Assuming the dataset is a square grid
    for i in range(0, len(dataset), row_length):
        row = [int(num) for num in dataset[i:i+row_length]]
        grid.append(row)
    return grid

# Example usage
dataset = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
grid = convert_to_grid(dataset)

start_time = time.time()
result = Suduko(grid, 0, 0)
end_time = time.time()

if result:
    print("Solution:")
    puzzle(grid)
    print("Total time used:", end_time - start_time, "seconds")
else:
    print("No solution found.")











































#WORKING. GOOGLE. UNOPTIMISED. (2)
#https://www.askpython.com/python/examples/sudoku-solver-in-python

M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False


    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Suduko(grid, row, col):

    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")






















#NOT working. AI HELP. (1)

import time

def solve_sudoku(grid):
    def is_valid(row, col, num):
        # Check if the number is valid in the given row
        for i in range(1,10):
            if grid[row][i] == num:
                return False

        # Check if the number is valid in the given column
        for i in range(9):
            if grid[i][col] == num:
                return False

        # Check if the number is valid in the given 3x3 sub-grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty_cell():
        # Find an empty cell in the grid
        for row in range(9):
            for col in range(9):
                if grid[row][col] == '.':
                    return row, col
        return None

    def solve():
        cell = find_empty_cell()
        if not cell:
            return True

        row, col = cell
        for num in '123456789':
            if is_valid(row, col, num):
                grid[row][col] = num

                if solve():
                    return True

                grid[row][col] = '.'  # Backtrack if the solution is not valid

        return False

    start_time = time.time()
    if solve():
        end_time = time.time()
        solve_time = end_time - start_time

        print("Solution:")
        for row in grid:
            print(' '.join(row))

        print("Time taken to solve: %.6f seconds" % solve_time)
    else:
        print("No solution exists.")




# User input for the Sudoku problem
user_input = input("Enter the Sudoku problem as a single string: ")

# Check if the input string has the required length
if len(user_input) != 81:
    print("Invalid input. The Sudoku string should have a length of 81.")
else:
    # Create the grid
    grid = [[user_input[i+j] for j in range(9)] for i in range(0, 81, 9)]

    # Solve and measure time
    solve_sudoku(grid)


