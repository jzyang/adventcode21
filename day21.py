#!/usr/bin/env python3
from sys import stdin

def parse_file():
    input = stdin.read().strip().split('\n')
    player1 = input[0].split(':')
    player2 = input[1].split(':')
    return int(player1[1].strip()), int(player2[1].strip())

def move_player(place, indices):
    sum_dice_rolls, next_indices = roll_dice(indices)
    if place + sum_dice_rolls > 10:
        current = (place + sum_dice_rolls) % 10
        if current == 0:
            current = 10
    else:
        current = place + sum_dice_rolls
    return current, next_indices

def roll_dice(start):
    moves = 0
    current = 0
    for i in range(3):
        if start + i > 100:
            current = (start + i) % 100
            if current == 0:
                current = 100
        else:
            current = (start + i)
        moves += current
    return moves, current + 1

def calc_result(p1_score, p2_score, rolled):
    if p1_score >= 1000:
        return p2_score * rolled
    else:
        return p1_score * rolled

def get_day_21_solutions():
    p1, p2 = parse_file()
    p1_score = 0
    p2_score = 0
    die = 1
    rolled = 0
    while p1_score < 1000 and p2_score < 1000:
        p1, die = move_player(p1, die)
        rolled += 3
        p1_score += p1
        if p1_score >= 1000:
            break
        p2, die = move_player(p2, die)
        rolled += 3
        p2_score += p2
        
        
#    print(p1_score)
#    print(p2_score)
#    print(rolled)
    print(calc_result(p1_score, p2_score, rolled))

get_day_21_solutions()
