# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/7#part2

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
    operator_list = [0] * l

    # Loop through each possible permutation of operators
    for _ in range(3 ** l):
        total = factors[0]   # Total of current equation
        # Execute the current equation
        for i, operator in enumerate(operator_list):
            if operator == 0:
                total += factors[i+1]
            elif operator == 1:
                total *= factors[i+1]
            else:   # Concatenation operator
                total = int(str(total) + str(factors[i+1]))

        if total == r:  # Success condition
            return True

        # Increment operators through base-3 counting system
        for j in range(l):
            if operator_list[j] < 2:
                operator_list[j] += 1
                break
            else:
                operator_list[j] = 0

    return False

print(solve("Day7/UnitTest.txt"))
print(solve("Day7/input.txt"))