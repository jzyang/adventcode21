#!/usr/bin/env python3

from sys import stdin
import math

def parse_fishes():
    return stdin.read().strip().split(',')

def reproduce(day, previous_day):
    current = previous_day.copy()
    total_fishes = len(current)
    for fish_day in range(total_fishes):
        if int(current[int(fish_day)]) > 0:
            current[int(fish_day)] = str(int(current[int(fish_day)]) - 1)
        else:
            current[int(fish_day)] = '6'
            current.append('8')
    return current

# Get the result
fishes = parse_fishes()
total_lanterns = 0
days = 80
for day in range(1, days + 1):
    fishes = reproduce(day, fishes)
    total_lanterns = len(fishes)


print(total_lanterns)
