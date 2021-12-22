#!/usr/bin/env python3
from sys import stdin

def parse_file():
    input = stdin.read().strip().split('\n')
    
    template = input[0]
    pairs = {}
    for index in range(len(template) - 1):
        pairs[template[index:index+2]] = 1
    
    dict = {}
    for line in input[2:]:
        pair, val = line.split(' -> ')
        dict[pair.strip()] = val.strip()
    
    return template, pairs, dict

def insert_by_step(pairs, total_cnt, dict):
    new_pairs = []
    delete_pairs = []
    for pair in pairs:
        insert_val = dict[pair]
            
        pair1 = pair[0] + insert_val
        pair2 = insert_val + pair[1]
        cnt = pairs[pair]
        add_to_dict(total_cnt, insert_val, cnt)
        
        # This pair is no longer needed
        delete_pairs.append(pair)
        
        # add new pairs
        new_pairs.append((pair1, cnt))
        new_pairs.append((pair2, cnt))
            
    delete(pairs, delete_pairs)
    
    for val in new_pairs:
        pair = val[0]
        cnt = val[1]
        add_to_dict(pairs, pair, cnt)

def diff_max_min(total_cnt):
    min = -1
    max = -1
    print(total_cnt)
    for key in total_cnt.keys():
        val = total_cnt[key]
        if min == -1 or val < min:
            min = val
        elif val > max:
            max = val
    
    return max - min
        
def add_to_dict(dict, key, val):
    if key in dict.keys():
        dict[key] += val
    else:
        dict[key] = val

def delete(dict, keys):
    for key in keys:
        dict.pop(key)

def count(line):
    letters = {}
    for letter in line:
        add_to_dict(letters, letter, 1)
    return letters

def sum_letters(total_cnt):
    total_letters = 0
    for letter in total_cnt.keys():
        total_letters += total_cnt[letter]
    return total_letters

def get_day_14_solutions():
    template, pairs, dict  = parse_file()
    total_cnt = count(template)
    for i in range(10):
        insert_by_step(pairs, total_cnt, dict)
    print("step 10: %d" % diff_max_min(total_cnt))
    for i in range(30):
        insert_by_step(pairs, total_cnt, dict)
    print("step 30: %d" % diff_max_min(total_cnt))

get_day_14_solutions()
