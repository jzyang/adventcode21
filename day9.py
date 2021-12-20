#!/usr/bin/env python3
from sys import stdin

def parse_file():
    return stdin.read().strip().split('\n')

# Generate a matrix from the given input
def generate_matrix(input):
    rows = len(input)
    cols = len(input[0])
    matrix = []
    for row in range(rows):
        line = input[row]
        new_row = []
        for col in range(cols):
            new_row.append(int(line[col]))
        matrix.append(new_row)
    return matrix

# Check if a given (row, col) in the matrix is the riskiest
# by looking around to see if there are riskier.
def is_risky(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    current = matrix[row][col]
    not_risky = False
    if row - 1 >= 0 and matrix[row - 1][col] < current:
        # check up and found something riskier
        return not_risky
    elif row + 1 < rows and matrix[row + 1][col] < current:
        # check down and found something riskier
        return not_risky
    elif col - 1 >= 0 and matrix[row][col - 1] < current:
        # check left and found something riskier
        return not_risky
    elif col + 1 < cols and matrix[row][col+1] <= current:
        # check right and found something riskier
        return not_risky
    return True

# Find all risks associated with this graph
def find_risks(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    risks = []
    basin_sizes = []
    
    traveled = init_size_map(matrix)
    
    for row in range(rows):
        for col in range(cols):
            if is_risky(matrix, row, col):
                # This is a nadier, there is no riskier, add it to the
                # risks list.
                risks.append(matrix[row][col] + 1)
                # Calculate the size
                basin_sizes.append(get_size(matrix, traveled, row, col))
    
    basin_sizes = sorted(basin_sizes)
    multiple = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    
    return sum(risks), multiple

# Check to see if we can find a way to keep going or if we're at a dead end
# for this part of the graph
def is_dead_end(matrix, row, col, dx, dy):
    rows = len(matrix)
    cols = len(matrix[0])
    current = matrix[row][col]
    not_dead_end = False
    if row + dx >= 0 and row + dx < rows and matrix[row + dx][col] < 9:
        print("is_dead_end row + dx")
        # check left/right and found an out
        return not_dead_end
    elif col + dy >= 0 and col + dy < cols and matrix[row][col + dy] < 9:
        print("is_dead_end col + dy")
        # check up/down and found an out
        return not_dead_end
    return True
    
def get_size(matrix, matrix_traveled, row, col):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Start from a given nadir and keep going until we find only dead ends;
    # Mark the map as we go
    in_basin = []
    traverse_adjacent_sides(matrix, matrix_traveled, in_basin, row, col, rows, cols)
    
    return len(in_basin)
    
def traverse_adjacent_sides(matrix, matrix_traveled, in_basin, row, col, rows, cols):
    if matrix[row][col] == 9 or matrix_traveled[row][col] >= 0:
        if matrix[row][col] == 9 and matrix_traveled[row][col] < 0:
            # It has no value because a wall is reached
            matrix_traveled[row][col] = 0
        return in_basin
        
    matrix_traveled[row][col] = 1
    if row + 1 < rows and matrix_traveled[row + 1][col] < 0:
        traverse_adjacent_sides(matrix, matrix_traveled, in_basin, row + 1, col, rows, cols)
    if row - 1 >= 0 and matrix_traveled[row - 1][col] < 0:
        traverse_adjacent_sides(matrix, matrix_traveled, in_basin, row - 1, col, rows, cols)
    if col + 1 < cols and matrix_traveled[row][col + 1] < 0:
        traverse_adjacent_sides(matrix, matrix_traveled, in_basin, row, col + 1, rows, cols)
    if col - 1 >= 0 and matrix_traveled[row][col - 1] < 0:
        traverse_adjacent_sides(matrix, matrix_traveled, in_basin, row, col - 1, rows, cols)
    
    if not (row, col) in in_basin:
        in_basin.append((row, col))
    
    return in_basin
 

def init_size_map(matrix):
    size = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    new_matrix = []
    for row in range(rows):
        new_matrix.append([0] * cols)
        for col in range(cols):
            new_matrix[row][col] = -1
    
    return new_matrix

def get_day_9_solutions():
    input = parse_file()
    heat_map = generate_matrix(input)
    sum_risks, basin_sizes = find_risks(heat_map)
    print("sum is %s" % (sum_risks))
    print("multiple is %s" % (basin_sizes))

get_day_9_solutions()
