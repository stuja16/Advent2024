# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/3#part2

import re

def solve(fileName):
    total = 0   # Final answer

    # Instructions start w/ inherent "do", and then we find subsequent commands
    lines = open(fileName,"r").read().strip().split('do()')
    for l in lines:
        total += processDoLine(l)

    return total

def processDoLine(line):
    total = 0

    text = line.split("don't()")
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", text[0]) # Only search the portion before a "don't" command
    for m in matches:
        total += getProduct(m)

    return total

# Takes the string value of a "mul" command and executes it
def getProduct(str):
    factors = list(map(int,re.findall("\d+",str)))  # Extract the two numbers into an integer list
    return factors[0]*factors[1]

print(solve("Day3/UnitTest2.txt"))
print(solve("Day3/input.txt"))