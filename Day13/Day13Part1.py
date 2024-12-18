# https://adventofcode.com/2024/day/13

# All coordinate changes from button presses are positive, so no need to worry about subtraction

import re

def solve(fileName):
    failCond = 500  # A token count high enough that it can never be hit on one machine
    tokens = 0
    # Input cleaning
    for cm in open(fileName,"r").read().strip().split("\n\n"):
        matches = [int(m) for m in re.findall("\d+", cm)]
        # failCond is the return value if a button sequence within the guidelines cannot be found: AKA 0 tokens should be spent
        nt = canGetPrize(matches,failCond)
        if nt < failCond: tokens += nt

    return tokens

def canGetPrize(cm,fail) -> int:
    min = fail
    for a in range(101):
        for b in range(101):
            if a*cm[0]+b*cm[2]==cm[4] and a*cm[1]+b*cm[3]==cm[5] and min>3*a+b:
                min = 3*a + b

    return min
    
print(solve("Day13/UnitTest.txt"))
print(solve("Day13/input.txt"))