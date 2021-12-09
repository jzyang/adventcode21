#!/usr/bin/env python3
from sys import stdin

def parse_file():
    return stdin.read().strip().split('\n')
    
def count_digits(digits, dict_letters_to_no, no_list):
    count = 0
    for digit in digits:
        if dict_letters_to_no[digit] in no_list:
            count +=1
    return count

def initialize_digits(input):
    chosen_digits = []
    letters_to_digits = []
    digits_to_letters = []
    decrypted_digits = []
    for index in range(len(input)):
        l_to_d, d_to_l, four, digit = get_digits(input[index])
        letters_to_digits.append(l_to_d)
        digits_to_letters.append(d_to_l)
        chosen_digits.append(four)
        decrypted_digits.append(digit)
    
    return letters_to_digits, digits_to_letters, chosen_digits, decrypted_digits

def get_include_exclude(digit1, digit2):
    include = []
    exclude = []
    digit1p = digit2p = ''
    if len(digit1) < len(digit2):
        digit1, digit2 = swap(digit1, digit2)
    for letter in digit1:
        if letter in digit2:
            include.append(letter)
        else:
            exclude.append(letter)
    return "".join(sorted(include)), "".join(sorted(exclude))

def swap(digit1, digit2):
    return digit2, digit1

def find_len_5(dict_digits, dict_known):
    include, exclude = get_include_exclude(dict_known[4], dict_known[1])
    for key in dict_digits:
        digit_len = len(key)
        if digit_len == 5:
            include1, exclude1 = get_include_exclude(key, dict_known[1])
            include_db, exclude_db = get_include_exclude(key, exclude)
            if include1 == dict_known[1]:
                dict_known[3] = key
                dict_digits[key] = 3
            elif include_db == exclude:
                dict_known[5] = key
                dict_digits[key] = 5
            else:
                dict_known[2] = key
                dict_digits[key] = 2
        
def find_len_6(dict_digits, dict_known):
    zero_nine = []
    for key in dict_digits:
        digit_len = len(key)
        if digit_len == 6:
            include1, exclude1 = get_include_exclude(key, dict_known[1])
            include4, exclude4 = get_include_exclude(key, dict_known[4])
            if include4 == dict_known[4]:
                dict_known[9] = key
                dict_digits[key] = 9
            elif include1 == dict_known[1]:
                dict_known[0] = key
                dict_digits[key] = 0
            else:
                dict_known[6] = key
                dict_digits[key] = 6

def get_digits(input):
    values = input.strip().split('|')
    digit_list = values[0].strip().split()
    chosen_digits = clean_encrypted_digits(values[1].strip().split())
    dict_all_digits, dict_known_digits = to_dict(digit_list)
    find_len_5(dict_all_digits, dict_known_digits)
    find_len_6(dict_all_digits, dict_known_digits)
    digit = to_digit(chosen_digits, dict_all_digits)
    
    # return the parsed values
    return dict_all_digits, dict_known_digits, chosen_digits, digit

def clean_encrypted_digits(list):
    for index in range(len(list)):
        list[index] = ''.join(sorted(list[index]))
    return list

def to_digit(digits, dict_letters_to_no):
    result = ''
    for digit in digits:
        result += str(dict_letters_to_no[digit])
    return int(result)
    
def to_dict(input):
    digit_len_cases = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    all_digits = {}
    known_digits = {}
    for encrypted in input:
        digit_val = digit_len_cases.get(len(encrypted), -1)
        sorted_encrypt = ''.join(sorted(encrypted))
        if digit_val > 0:
            known_digits[digit_val] = sorted_encrypt
        all_digits[sorted_encrypt] = digit_val
    return all_digits, known_digits

def get_day_8_solutions():
    input = parse_file()
    dict_letters_to_no, dict_no_to_letters, chosen_digits, digits = initialize_digits(input)
    
    count = 0
    sum = 0
    for index in range(len(digits)):
        count += count_digits(chosen_digits[index], dict_letters_to_no[index],  [1, 4, 7, 8])
        sum += digits[index]
    print("Total times digits: 1, 4, 7 or 8 appeared: %s" % (count))
    print("Sum is: %d" % (sum))
    

get_day_8_solutions()
