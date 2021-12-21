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

def insert_by_step(template, pairs, dict, total_cnt):
    new_pairs = []
    new_template = ''
    for index in range(len(template) - 1):
        pair = template[index:index+2]
        insert_val = dict[pair]
        add_to_dict(total_cnt, insert_val)
        if index == 0:
            new_template += pair[0] + insert_val + pair[1]
        else:
            new_template += insert_val + pair[1]
            
    for index in range(len(new_template) - 1):
        pair = new_template[index:index+2]
        add_to_dict(pairs, pair)
    
    return new_template

def count_letters(template):
    total_cnt = {}
    for letter in template:
        add_to_dict(total_cnt, letter)
    
    return total_cnt

def diff_max_min(total_cnt):
    min = 999
    max = 0
    for key in total_cnt.keys():
        val = total_cnt[key]
        if val < min:
            min = val
        elif val > max:
            max = val
    
    return max - min

def add_to_dict(dict, key):
    if key in dict.keys():
        dict[key] += 1
    else:
        dict[key] = 1

def get_day_14_solutions():
    template, pairs, dict  = parse_file()
    print(template)
    new_template = template
    total_cnt = count_letters(new_template)
    print(pairs)
    print(total_cnt)
    for i in range(40):
        new_template = insert_by_step(new_template, pairs, dict, total_cnt)
        if i == 9:
            print(diff_max_min(total_cnt))
            break
    print(diff_max_min(total_cnt))

get_day_14_solutions()
