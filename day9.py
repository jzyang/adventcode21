#!/usr/bin/env python3
from sys import stdin

def parse_file():
    return stdin.read().strip().split('\n')

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

def find_risks(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    risks = []
    basin_sizes = []
    
    traveled = init_size_map(matrix)
    
    for row in range(rows):
        for col in range(cols):
            if is_risky(matrix, row, col):
                risks.append(matrix[row][col] + 1)
                basin_sizes.append(get_size(matrix, traveled, row, col))
    
    return sum(risks), basin_sizes

def find_basins(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    risks = []
    for row in range(rows):
        for col in range(cols):
            if is_risky(matrix, row, col):
                risks.append(matrix[row][col] + 1)
    return sum(risks)

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
    size = 0
    
    if row - 1 >= 0 and matrix[row - 1][col] != 9 and added[row-1][col] == 0:
        size += dfs(matrix, added, row, col, -1, 0)
    if row + 1 < rows and matrix[row + 1][col] != 9 and added[row+1][col] == 0:
        size += dfs(matrix, added, row, col, 1, 0)
    if col - 1 >= 0 and matrix[row][col - 1] != 9 and added[row][col-1] == 0:
        size += dfs(matrix, added, row, col-1, size)
    if col + 1 < cols and matrix[row][col+1] != 9 and added[row][col+1] == 0:
        size += dfs(matrix, added. row, col + 1, size)
    print(size)
    
def dfs(matrix, added, row, col, drow, dcol):
    
   if matrix[row + drow][col + dcol] != 9:
        if row + drow >= 0
         and matrix[row + drow][col + dcol]
        dfs(matrix, row, col, )
    elif:
        
    
    

def init_size_map(matrix):
    size = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    new_matrix = []
    for row in range(rows):
        new_matrix.append([0] * cols)
    
    return new_matrix

def get_day_9_solutions():
    input = parse_file()
    heat_map = generate_matrix(input)
    sum_risks, basin_sizes = find_risks(heat_map)
    print("sum is %s" % (sum_risks))
#    multiply_top_3_basins = find_basins(basin_sizes)
    print("multiple is %s" % (basin_sizes))

get_day_9_solutions()
