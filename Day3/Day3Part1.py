# https://adventofcode.com/2024/day/3

import re

def solve(fileName):
    total = 0   # Final answer

    data = open(fileName,"r").read().strip()
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", data)
    for m in matches:
        total += getProduct(m)

    return total

def getProduct(str):
    factors = list(map(int,re.findall("\d+",str)))  # Extract the two numbers into an integer list
    return factors[0]*factors[1]

print(solve("Day3/UnitTest.txt"))
print(solve("Day3/input.txt"))