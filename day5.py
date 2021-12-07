#!/usr/bin/env python3

from sys import stdin

def parse_coords():
    return stdin.read().strip().split('\n')

def swap(x, y):
    return y, x

def get_y(vent_dict, x):
    if x in vent_dict:
        y_dict = vent_dict[x]
    else:
        y_dict = {}
    return y_dict

def find_vents_y(vent_dict, x, y1, y2):
    # Make sure the range is in increasing order
    if int(y1) > int(y2):
        y1, y2 = swap(y1, y2)
    y_dict = get_y(vent_dict, x)
    for y in range(int(y1),int(y2) + 1):
        if str(y) in y_dict:
            y_dict[str(y)] += 1
        else:
            y_dict[str(y)] = 1
    return y_dict

def find_vents_x(vent_dict, x1, x2, y):
    # Make sure the range is in increasing order
    if int(x1) > int(x2):
        x1, x2 = swap(x1, x2)
    for x in range(int(x1),int(x2) + 1):
        # Correctly set the dictionary of ys
        y_dict = get_y(vent_dict, str(x))
        # check if there's already an existing vent
        if y in y_dict:
            y_dict[y] += 1
        else:
            y_dict[y] = 1
        vent_dict[str(x)] = y_dict

def find_vents_diag(vent_dict, x1, x2, y1, y2):
    if int(x1) > int(x2):
        x1p = int(x1)
        x2p = int(x2) - 1
        dx = -1
    else:
        x1p = int(x1)
        x2p = int(x2) + 1
        dx = 1
        
    if int(y1) > int(y2):
        dy = -1
    else:
        dy = 1
    
    y = int(y1)
    for x in range(x1p, x2p, dx):
        # Correctly set the dictionary of ys
        y_dict = get_y(vent_dict, str(x))
        # check if there's already an existing vent
        if str(y) in y_dict:
            y_dict[str(y)] += 1
        else:
            y_dict[str(y)] = 1
        vent_dict[str(x)] = y_dict
        y += dy

def create_vent_dict(vents, include_diagonal):
    vent_dict = {}
    y_dict = {}
    for vent in vents:
        start, end = vent.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        if x1 == x2:
            vent_dict[x1] = find_vents_y(vent_dict, x1, y1, y2)
        elif y1 == y2:
            find_vents_x(vent_dict, x1, x2, y1)
        elif include_diagonal and abs(int(x1) - int(x2)) == abs(int(y1) - int(y2)):
            find_vents_diag(vent_dict, x1, x2, y1, y2)
    return vent_dict

# Get the result
vents = parse_coords()
vent_dict_linear = create_vent_dict(vents, False)
vent_dict_all = create_vent_dict(vents, True)

danger_linear = 0
for x in sorted(vent_dict_linear.keys()):
    for y in sorted(vent_dict_linear[x].keys()):
        if vent_dict_linear[x][y] > 1:
            danger_linear += 1

danger_all = 0
for x in sorted(vent_dict_all.keys()):
    for y in sorted(vent_dict_all[x].keys()):
        if vent_dict_all[x][y] > 1:
            danger_all += 1
            
print("linear danger: %d" % (danger_linear))
print("all dangers: %d" % (danger_all))
