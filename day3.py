#!/usr/bin/env python3

from sys import stdin

def parseFile():
    return stdin.read().strip().split('\n')
  
def get_bit(value, bit_index):
    return value >> bit_index & (1 << 0)

def get_most_popular_bits(bitsInput):
    # Set initial values
    total = len(bitsInput)
    mid = total >> 1
    bitLen = len(bitsInput[0])
    result = ''
    for lengthIndex in range(bitLen):
        sum = 0
        for index in range(total):
            sum += get_bit(int(bitsInput[index], 2), lengthIndex)
        if sum > mid:
            result = '1' + result
        else:
            result = '0' + result
    # Calculate the requested vars
    gamma = int(result, 2)
    epsilon = int(result, 2) ^ int('1' * len(result), 2)
    power_consumption = gamma * epsilon
    # Output result
    print(power_consumption)

def get_life_support_rating(bitsInput):
    # Set initial values
    oxyBits = bitsInput
    co2Bits = bitsInput
    bitLen = len(bitsInput[0])
    for ind in range(bitLen - 1, -1, -1):
        if len(oxyBits) == 1 and len(co2Bits) == 1:
            break
        if len(oxyBits) > 1:
            oxyBits = oxy_check(oxyBits, ind)
        if len(co2Bits) > 1:
            co2Bits = co2_check(co2Bits, ind)
    # Find life-support rating
    life_support_rating = int(oxyBits[0], 2) * int(co2Bits[0], 2)
    print(life_support_rating)

def oxy_check(bits, shift):
    sum = 0
    total = len(bits)
    # Calculate the midpoint
    if total % 2 == 1:
        mid = (total + 1) >> 1
    else:
        mid = total >> 1
    # Get the sum and filter based on max
    for index in range(total):
        sum += get_bit(int(bits[index], 2), shift)
    if sum >= mid:
        return filter_bits(bits, shift, 1)
    else:
        return filter_bits(bits, shift, 0)

def co2_check(bits, shift):
    sum = 0
    total = len(bits)
    # Calculate the midpoint
    if total % 2 == 1:
        mid = (total + 1) >> 1
    else:
        mid = total >> 1
    # Get the sum and filter based on max
    for index in range(total):
        sum += get_bit(int(bits[index], 2), shift)
    if sum < mid:
        return filter_bits(bits, shift, 1)
    else:
        return filter_bits(bits, shift, 0)
    
def filter_bits(bits, shift, value):
    result = list(filter(lambda b: ( get_bit(int(b, 2), shift) == value ), bits))
    return result


# Get the result
bits = parseFile()
print("What is the power consumption of the submarine?")
get_most_popular_bits(bits)
print("What is the life support rating of the submarine?")
get_life_support_rating(bits)
