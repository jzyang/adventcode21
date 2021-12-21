#!/usr/bin/env python3
from sys import stdin

def parse_file():
    lines = stdin.read().strip().split('\n')
    
    coords = []
    steps = 0
    x_max = 0
    y_max = 0
    for coord in lines:
        steps += 1
        if len(coord) == 0:
            # Folds are next
            break
        x, y = coord.split(',')
        coords.append((int(x), int(y)))
        if int(x) > x_max:
            x_max = int(x)
        if int(y) > y_max:
            y_max = int(y)
    coords = sorted(coords)

    folds = []
    for line in lines[steps:]:
        fold = line[10:]
        axis, coord = fold.split('=')
        folds.append((axis, int(coord)))
        
    return coords, x_max, y_max, folds

# Generate a matrix from the given input
def generate_matrix(coords, rows, cols):
    matrix = []
    for x in range(rows):
        new_row = []
        for y in range(cols):
            if (x, y) in coords:
                new_row.append('#')
            else:
                new_row.append('.')
        matrix.append(new_row)
    return matrix

def count_pts(matrix, rows, cols):
    pts = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '#':
                pts += 1

    return pts

def fold(matrix, fold_instr):
    axis, val = fold_instr
    if axis.strip() == 'x':
        return fold_x(matrix, val)
    else:
        return fold_y(matrix, val)

def fold_x(matrix, val):
    rows = len(matrix)
    cols = len(matrix[0])
    
    new_matrix = []
    max_traverse = cols - val
    index = val + 1
    for row in range(val - 1, -1, -1):
        if index >= rows:
            break
        new_row = matrix[row]
        second_half_matrix = matrix[index]
        for x in range(len(matrix[row])):
            if new_row[x] == '.' and second_half_matrix[x] == '#':
                new_row[x] = second_half_matrix[x]
        new_matrix.append(new_row)
        index += 1
    
    return new_matrix

def fold_y(matrix, val):
    rows = len(matrix)
    cols = len(matrix[0])
    
    new_matrix = []
    max_traverse = cols - val
    for row in range(rows):
        new_row = matrix[row][0:val]
        second_half_matrix = matrix[row][val + 1:]
        index = 0
        for col in range(val, 0, -1):
            if index >= len(second_half_matrix):
                break
            if new_row[col - 1] == '.' and second_half_matrix[index] == '#':
                new_row[col - 1] = second_half_matrix[index]
            index += 1
        new_matrix.append(new_row)
    
    return new_matrix

def fold_all(matrix, folds):
    new_matrix = matrix
    for fold_instr in folds:
        new_matrix = fold(new_matrix, fold_instr)
    
    return new_matrix
    
def output(code):
    rows = len(code)
    cols = len(code[0])
    
    for col in range(cols):
        line = []
        for row in range(rows):
            line.append(code[row][col])
        print(line)

def output_backwards(code):
    rows = len(code)
    cols = len(code[0])
    
    for col in range(cols):
        line = []
        for row in range(rows):
            line.append(code[rows - row - 1][col])
        print(line)

def get_day_13_solutions():
    coords, xs, ys, folds = parse_file()
    rows = xs + 1
    cols = ys + 1
    matrix = generate_matrix(coords, rows, cols)
    pts = count_pts(matrix, rows, cols)
    after_fold = fold(matrix, folds[0])
    pts = count_pts(after_fold, len(after_fold), len(after_fold[0]))
    print(pts)
    
    code = fold_all(matrix, folds)
#    output(code)
    output_backwards(code)

get_day_13_solutions()
