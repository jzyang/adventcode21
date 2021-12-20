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
    
def init_flashed(matrix):
    size = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    new_matrix = []
    for row in range(rows):
        new_matrix.append([0] * cols)
        for col in range(cols):
            new_matrix[row][col] = 0
    
    return new_matrix
    
def simulate_steps(steps, dumbos):
#    print("Before any steps:")
#    print(dumbos)
    
    rows = len(dumbos)
    cols = len(dumbos[0])
    flash_cnt = 0
    for step in range(steps):
        step_flash = init_flashed(dumbos)
        flash_cnt += step_change(dumbos, step_flash, rows, cols)
#        print("After step %s: %s" % (step + 1, flash_cnt))
#        print(dumbos)
    
    return flash_cnt

def step_change(dumbos, flashed, rows, cols):
    for row in range(rows):
        for col in range(cols):
            dfs_increment(dumbos, flashed, row, col, rows, cols)
    
    return count_flashes(dumbos, rows, cols)

def dfs_increment(dumbos, flashed, row, col, rows, cols):
    if flashed[row][col] == 1:
        # skip
        return

    dumbos[row][col] += 1
    if dumbos[row][col] <= 9:
        return
    
    if dumbos[row][col] > 9 and flashed[row][col] == 0:
        # Flash
        flashed[row][col] = 1
        dumbos[row][col] = 0
        if row + 1 < rows and flashed[row + 1][col] < 1:
            dfs_increment(dumbos, flashed, row + 1, col, rows, cols)
        if row - 1 >= 0 and flashed[row - 1][col] < 1:
            dfs_increment(dumbos, flashed, row - 1, col, rows, cols)
        if col + 1 < cols and flashed[row][col + 1] < 1:
            dfs_increment(dumbos, flashed, row, col + 1, rows, cols)
        if col - 1 >= 0 and flashed[row][col - 1] < 1:
            dfs_increment(dumbos, flashed, row, col - 1, rows, cols)
        if row + 1 < rows and col + 1 < cols and flashed[row + 1][col + 1] < 1:
            dfs_increment(dumbos, flashed, row + 1, col + 1, rows, cols)
        if row - 1 >= 0 and col + 1 < cols and flashed[row - 1][col + 1] < 1:
            dfs_increment(dumbos, flashed, row - 1, col + 1, rows, cols)
        if row + 1 < rows and col - 1 >= 0 and flashed[row + 1][col - 1] < 1:
            dfs_increment(dumbos, flashed, row + 1, col - 1, rows, cols)
        if row - 1 >= 0 and col - 1 >= 0 and flashed[row - 1][col - 1] < 1:
            dfs_increment(dumbos, flashed, row - 1, col - 1, rows, cols)

def count_flashes(dumbos, rows, cols):
    flashes = 0
    for row in range(rows):
        for col in range(cols):
            if dumbos[row][col] == 0:
                flashes += 1

    return flashes

def find_steps(dumbos):
    flashes = 0
    steps = 0
    while flashes != 100:
        steps += 1
        flashes = simulate_steps(1, dumbos)

    return steps

def get_day_11_solutions():
    input = parse_file()
    dumbos = generate_matrix(input)
    flash_cnt = simulate_steps(100, dumbos)
    print("flashes %s" % (flash_cnt))
    dumbos = generate_matrix(input)
    steps = find_steps(dumbos)
    print("It took %s steps to achieve synchronizination" % (steps))
    
get_day_11_solutions()
