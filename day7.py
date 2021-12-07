#!/usr/bin/env python3

from sys import stdin

def parseFile():
    return stdin.read().strip().split(',')

def initialize():
    where_the_crabs_at = parseFile()
    for index in range(len(where_the_crabs_at)):
        where_the_crabs_at[index] = int(where_the_crabs_at[index])
    where_the_crabs_at.sort(reverse=True)
    return where_the_crabs_at

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
    most_strategic = -1
    crabbiest = crabs[0]
    dist_dict = {}
    for crab_pos in range(crabbiest):
        fuel = 0
        for position in crabs:
            if most_strategic > 0 and fuel > most_strategic:
                break
            else:
                fuel += sum_position(dist_dict, abs(position - crab_pos))
        if fuel < most_strategic or most_strategic < 0:
            most_strategic = fuel
            best_position = crab_pos
    return best_position, most_strategic
    
def get_most_strategic():
    where_the_crabs_at = initialize()
    best_position, most_strategic = get_best(where_the_crabs_at)
    print("The most crab-tastic position is %s and it will take %s fuel to align" % (best_position, most_strategic))

get_most_strategic()
