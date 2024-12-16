# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/8#part2

import re

def solve(fileName):
    antennas = {}
    antinodes = set()

    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    # Search the input for all antennas & log their frequency & coords
    for y,x in grid:
        val = grid[y,x]
        if not val == ".":
            if val in antennas:
                antennas[val].append((y,x))
            else:
                antennas[val] = [(y,x)]

    # Go through each frequency to find all valid antinodes
    for freq in antennas:
        coordPairs = antennas[freq]
        if len(coordPairs) > 1:
            findAntinodes(h, w, coordPairs, antinodes)

    return len(antinodes)

# Takes a list of antennas that all have the same frequency, "f"
# Finds a list of all valid antinodes for the given antennas that are within the given area, and adds them to the set
def findAntinodes(h, w, antennas, validAnts):
    # Add all antennas to the antinodes list
    for a in antennas:
        validAnts.add(a)

    # Cycle through every pair of antennas
    for a1 in range(len(antennas)-1):
        for a2 in range(a1+1,len(antennas)):
            y1,x1 = antennas[a1]
            y2,x2 = antennas[a2]
            dy,dx = y1-y2,x1-x2
            
            # Validate antidotes: valid if they are within the dimensions of the input
            searchLine(y1, x1, dy, dx, h, w, validAnts)
            searchLine(y2, x2, -dy, -dx, h, w, validAnts)

# Recursive function that checks for all valid antinodes on the given line
def searchLine(y, x, dy, dx, h, w, validAnts):
    if 0 <= y+dy < h and 0 <= x+dx < w: # If within dimensions, log and check the next point on the line
        validAnts.add((y+dy,x+dx))
        searchLine(y+dy, x+dx, dy, dx, h, w, validAnts)
    
print(solve("Day8/UnitTest.txt"))
print(solve("Day8/input.txt"))