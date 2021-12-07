#!/usr/bin/env python3

from sys import stdin

def parse_file():
    return stdin.read().strip().split(',')

def initialize():
    where_the_crabs_at = parse_file()
    for index in range(len(where_the_crabs_at)):
        where_the_crabs_at[index] = int(where_the_crabs_at[index])
    where_the_crabs_at.sort(reverse=True)
    return where_the_crabs_at

def sum_position(dict_deltas, delta):
    if delta in dict_deltas:
        return dict_deltas[delta]
    sum = 0
    for dist in range(delta + 1):
        sum += dist
    dict_deltas[delta] = sum
    return sum

def get_best(crabs, is_fuel_constant):
    most_strategic = -1
    best_position = 0
    crabbiest = crabs[0]
    dist_dict = {}
    for crab_pos in range(crabbiest):
        fuel = 0
        for position in crabs:
            if most_strategic > 0 and fuel > most_strategic:
                break
            elif is_fuel_constant:
                fuel += abs(position - crab_pos)
            else:
                fuel += sum_position(dist_dict, abs(position - crab_pos))
        if fuel < most_strategic or most_strategic < 0:
            most_strategic = fuel
            best_position = crab_pos
    return best_position, most_strategic
    
def get_most_strategic():
    is_fuel_constant = True
    where_the_crabs_at = initialize()
    best_position, most_strategic = get_best(where_the_crabs_at, is_fuel_constant)
    print("When fuel is constant, a crab-tastic start would be at %s with %s fuel cells." % (best_position, most_strategic))
    best_position, most_strategic = get_best(where_the_crabs_at, not is_fuel_constant)
    print("Otherwise, when fuel is not constant, start at %s with %s fuel cells." % (best_position, most_strategic))

get_most_strategic()
