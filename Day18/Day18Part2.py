# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/18#part2

# Takes a few seconds to run
# Could obvi be optimized, but it's fast enough for me

import re
from heapq import heappop, heappush

def solve(fileName,memSize):
    input = open(fileName,"r").read().strip().split("\n")
    bytes = set()

    for bytesFallen in range(len(input)):
        for i in range(bytesFallen):
            x,y = [int(m) for m in re.findall("-?\d+", input[i])]
            bytes.add((x,y))

        # Modified from djikstra algo in Day16Part1
        startPos = (0,0)
        minScore = float('inf')

        # Setup data structures
        pq = []             # Min queue of valid ways to continue the path
        heappush(pq,(0,startPos))
        visited = set()     # Track visited coords to prevent loops/repeats
        visited.add(startPos)

        # Run djikstra
        while pq:
            curScore, (x,y) = heappop(pq)

            # Skip if out of range of memory-space
            if y < 0 or x < 0 or y > memSize or x > memSize:
                continue

            # Break if end of path
            if y==memSize and x==memSize:
                minScore = min(minScore, curScore)
                break

            # Move to adjacent cells:
            downPos = (x,y+1)
            upPos = (x,y-1)
            leftPos = (x-1,y)
            rightPos = (x+1,y)
            if downPos not in visited and downPos not in bytes:
                heappush(pq,(curScore+1,downPos))
                visited.add(downPos)
            if upPos not in visited and upPos not in bytes:
                heappush(pq,(curScore+1,upPos))
                visited.add(upPos)
            if leftPos not in visited and leftPos not in bytes:
                heappush(pq,(curScore+1,leftPos))
                visited.add(leftPos)
            if rightPos not in visited and rightPos not in bytes:
                heappush(pq,(curScore+1,rightPos))
                visited.add(rightPos)

        if minScore == float('inf'):
            return input[bytesFallen - 1]   # Return coords of byte that cut off last path

    return "failed"

print(solve("Day18/UnitTest.txt",6))
print(solve("Day18/input.txt",70))