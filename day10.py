#!/usr/bin/env python3
from sys import stdin

def parse_file():
    return stdin.read().strip().split('\n')

def stack_check(stacks):
    left_paren = ['(', '[', '{', '<']
    right_paren = [')', ']', '}', '>']
    
    corrupted_err_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    
    incomplete_err_dict = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    
    corrupted_score = 0
    incomplete_scores = []
    for line_no in range(len(stacks)):
        stack = []
        line = stacks[line_no]
        corrupt_err  = 0
        for paren in line:
            try:
                index = left_paren.index(paren)
                stack.append(paren)
            except:
                # Is a closing bracket
                corrupt_err = calc_corrupt(paren, stack, left_paren, right_paren, corrupted_err_dict)
                if corrupt_err > 0:
                    # Not the correct closing bracket
                    corrupted_score += corrupt_err
                    break
        if is_incomplete(corrupt_err):
            incomplete_scores.append(cal_incomplete(stack, left_paren, right_paren, incomplete_err_dict))
    
    incomplete_score = get_median(incomplete_scores)
    return corrupted_score, incomplete_score
    
def calc_corrupt(close, stack, open_paren, close_paren, err_dict):
    stack_len = len(stack)
    if stack_len == 0:
        # Nothing to pop, so this paren is an error
        return err_dict.get(paren, 0)
    
    og_stack = str(stack)
    open = stack.pop()
    open_index = open_paren.index(open)
    close_index = close_paren.index(close)
    if open_index == close_index:
        return 0
    
    # Mismatch found
    return err_dict.get(close, 0)

def is_incomplete(is_corrupt_err):
    if is_corrupt_err > 0:
        return False
        
    return True

def cal_incomplete(stack, open_paren, close_paren, err_dict):
    score = 0
    while len(stack) > 0:
        open = stack.pop()
        open_index = open_paren.index(open)
        close = close_paren[open_index]
        score = score * 5 + err_dict.get(close)
    return score
    
def get_median(scores):
    scores.sort()
    score_cnt = len(scores)
    mid = int( (score_cnt - 1) / 2 )
    return scores[mid]

def get_day_10_solutions():
    input = parse_file()
    corrupt, incomplete = stack_check(input)
    print(corrupt)
    print(incomplete)

get_day_10_solutions()
