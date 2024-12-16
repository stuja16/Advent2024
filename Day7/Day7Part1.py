# https://adventofcode.com/2024/day/7

import re

def solve(fileName):
    total = 0   # Final result

    lines = open(fileName,"r").read().strip().split("\n")
    for l in lines:
        total += processLine(l)

    return total

def processLine(line):
    result, *factors = list(map(int,re.findall("\d+", line)))

    if canBeProduced(result,factors):
        return result

    return 0

# Returns boolean: True if r can be produced by inserting + and * operators
def canBeProduced(r,factors):
    l = len(factors) - 1    # One less operator than factors
    operator_list = [False] * l

    # Loop through each possible permutation of operators
    for _ in range(2 ** l):
        total = factors[0]   # Total of current equation
        # Execute the current equation
        for i, operator in enumerate(operator_list):
            if operator:
                total += factors[i+1]
            else:
                total *= factors[i+1]

        if total == r:  # Success condition
            return True

        # Increment operators
        for j in range(l):
            if operator_list[j] == False:
                operator_list[j] = True
                break
            else:
                operator_list[j] = False

    return False
    
print(solve("Day7/UnitTest.txt"))
print(solve("Day7/input.txt"))