#!/usr/bin/env python3

from sys import stdin

def parseFile():
    return stdin.read().strip().split(',')

def initialize():
    crab_positions = parseFile()
    for index in range(len(crab_positions)):
        crab_positions[index] = int(crab_positions[index])
    crab_positions.sort(reverse=True)
    return crab_positions

def sum_position(dict_distance, delta):
    if delta in dict_distance:
        return dict_distance[delta]
    sum = 0
    for dist in range(delta + 1):
        sum += dist
    dict_distance[delta] = sum
    return sum

def get_best(crabs):
    best_position = -1
    best_fuel = -1
    max_position = crabs[0]
    dist_dict = {}
    for crab in range(max_position):
        fuel = 0
        for position in crabs:
            if best_fuel > 0 and fuel > best_fuel:
                break
            else:
                fuel += sum_position(dist_dict, abs(position - crab))
        if fuel < best_fuel or best_fuel < 0:
            best_fuel = fuel
            best_position = position
    return best_position, best_fuel
    
def get_best_fuel():
    crab_positions = initialize()
    best_position, best_fuel = get_best(crab_positions)
    print(best_fuel)

get_best_fuel()
