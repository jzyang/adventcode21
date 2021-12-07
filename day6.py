#!/usr/bin/env python3

from sys import stdin
import math

def parse_fishes():
    return stdin.read().strip().split(',')

def initialize(fishes):
    life_stage = [0] * 9
    for fish in fishes:
        # increment the number of fish at that life stage
        life_stage[int(fish)] += 1
    return life_stage

def next_day(life_stage_cycle):
    new_life = [0] * 9
    day_0_lanterns = life_stage_cycle[0]
    for day in range(8):
        new_life[day] = life_stage_cycle[day + 1]
    # Add the lanterns that's gone through their full cycle to
    # those that are on day 6 of their lives (from day 7)
    new_life[6] += day_0_lanterns
    # These are the new baby lanterns day 0s produced
    new_life[8] = day_0_lanterns
    return new_life


def reproduce(days, fishes):
    life_stage = initialize(fishes)
    for day in range(days):
        life_stage = next_day(life_stage)
    return sum(life_stage)

def calculate_lanterns():
    day = 80
    fishes = parse_fishes()
    total_lanterns = reproduce(day, fishes)
    print("%s: %s lantern fishes" % (day, total_lanterns))
    day = 256
    total_lanterns = reproduce(day, fishes)
    print("%s: %s lantern fishes" % (day, total_lanterns))

calculate_lanterns()
