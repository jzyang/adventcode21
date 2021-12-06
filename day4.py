#!/usr/bin/env python3

from sys import stdin

def parse_cards():
    return stdin.read().strip().split('\n')

def find_bingo_in_card(card, num, res):
    for line_no in range(len(card)):
        try:
            index = card[line_no].strip().split().index(num)
            bin = list(res[line_no])
            bin[index] = '1'
            res[line_no] = "".join(bin)
            break
        except:
            # in another line
            continue
    return res

def initialize(cards, nums):
    res = []
    # initialize board
    for line in cards:
        if len(line.strip()) == 0:
            res.append('')
        else:
            res.append('0' * len(line.strip().split()))
    return res

def find_bingo_nums(cards, nums, res):
    for num in nums:
        for start in range(0, len(cards), 6):
            end = start + 6
            res[start:end] = find_bingo_in_card(cards[start:end], num, res[start:end])
    return res

    
def find_bingo_num(cards, num, res, found_bingo, win_condition):
    for start in range(0, len(cards), 6):
        end = start + 6
        res[start:end] = find_bingo_in_card(cards[start:end], num, res[start:end])
        found_bingo[int(start/6)] = is_bingo(res[start:end])
        if win_condition(found_bingo):
            return res, found_bingo, start
    return res, found_bingo, 0
        
def is_bingo(res):
    # Check any across bingos
    for line in res:
        if len(line) == 0:
            continue
        if line == '1' * len(line):
            return '1'
    # Check vertical bingos
    for shift in range(5):
        sum = 0
        for line in res:
            if len(line) == 0:
                continue
            sum += get_bit(int(line, 2), shift)
        if sum == 5:
            return '1'
    return '0'
   
def get_bit(value, bit_index):
    return value >> bit_index & (1 << 0)
    
def win_condition_you(found_bingo):
    if '1' in found_bingo:
        return True
    return False

def win_condition_octopus(found_bingo):
    if '0' in found_bingo:
        return False
    return True

# Get the result
bingo = parse_cards()
bingo_no = bingo[0].split(',')
bingo = bingo[2:]

bits_bingo = initialize(bingo, bingo_no)
bits_bingo = find_bingo_nums(bingo, bingo_no[0:5], bits_bingo)

# Track which cards have bingo; 0 means no bingo
found_bingo = list('0' * (bingo.count('') + 1))

starting = 5
found_bingo_no = -1
bingo_card_start = 0
win_condition = win_condition_octopus
for lookup in bingo_no[starting:]:
    if not win_condition(found_bingo):
        # Have not found a bingo
        bits_bingo, found_bingo, bingo_card_start = find_bingo_num(bingo, lookup, bits_bingo, found_bingo, win_condition)
    if win_condition(found_bingo):
        found_bingo_no = int(lookup)
        break;

sum = 0
for index in range(5):
    bits_line = bits_bingo[bingo_card_start + index]
    if bits_line == '1' * len(bits_line):
        continue
    
    line = bingo[bingo_card_start + index].split()
    for num_index in range(len(line)):
        if bits_line[num_index] == '0':
            sum += int(line[num_index])

print(sum)
print(found_bingo_no)
print(sum * found_bingo_no)
